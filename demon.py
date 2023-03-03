import json
import time
import water

class Deamon():

    def __init__(self) -> None:
        self.load_db()
        self.last_watered = self.db["water_log"][-1][0]

    def start(self):
        while True:
            now = time.time()
            self.load_db()
            if (now - self.last_watered) >= self.watering_period:
                water.water(self.water_for)
                self.last_watered = now
                self.update_db(now)
            time.sleep((self.last_watered + self.watering_period) - now)

    def update_db(self, time_of_watering):
        """Update db record."""
        success = False
        while not success:
            try:
                with open("./db.json", "w") as db_w:
                    self.db["water_log"].append([time_of_watering, self.water_for])
                    json.dump(self.db, db_w, indent=4)
                success = True
            except Exception:
                pass

    def load_db(self):
        success = False
        while not success:
            try:     
                with open("./db.json", "r") as db_file:
                    self.db = json.load(db_file)
                self.watering_period = self.db["watering_period_s"]
                self.water_for = self.db["water_for_s"]
                success = True
            except Exception:
                pass


    
