import os
import json
import demon

from multiprocessing import Process
from flask import Flask, redirect, request, render_template
from water import water 

class Server():
    
    def __init__(self):
        self.demon_proces = None
        self.load_stored_data()
        self.instantiate_demon()
    
    def load_stored_data(self):
        with open("./db.json", 'r') as f:
            self.db = json.load(f)

    def update_stored_data(self, watering_period_s, water_for_s):
        self.load_stored_data()
        self.db["watering_period_s"] = watering_period_s
        self.db["water_for_s"] = water_for_s

        with open("./db.json", "w") as f:
            json.dump(self.db, f, indent=4)

    def instantiate_demon(self):
        self.demon = demon.Deamon()
        self.demon_proces = Process(target=self.demon.start)
        self.demon_proces.start()


########### APP SHIT ###########    

app = Flask(__name__)

server = Server()
host_ip = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]

@app.route('/')
def index():
    return render_template('index.html', display_popup="none", hours=0)

@app.route('/<setted_value>')
def index_w_set( setted_value):
    return render_template('index.html', display_popup="block", nastaveno_dni=setted_value)

@app.route('/set_period', methods=['POST', 'GET'])
def set_period():
    try:
        if request.method == 'POST':
            watering_period = int(request.form['watering_period']) * 1440
            water_for = int(request.form["water_for"])
            water_thread = Process(target=water, daemon=True,  args=(water_for,))
            print(water_for, water)
            water_thread.start()
            server.update_stored_data(watering_period, water_for)
            return redirect("/" + str(round(watering_period/1440)))
    except Exception as e:
        print(e)
        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, host=host_ip)