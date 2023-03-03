function fadeOutEffect() {
    let duration = 6
    var fadeTarget = document.getElementById("popup");
    var fadeEffect = setInterval(function () {
        if (!fadeTarget.style.opacity) {
            fadeTarget.style.opacity = 1;
        }
        if (fadeTarget.style.opacity > 0) {
            fadeTarget.style.opacity -= 0.01;
        } else {
            clearInterval(fadeEffect);
        }
    }, duration*10);
}
window.addEventListener('load', (event) => {
    fadeOutEffect()
    document.getElementById("submitButton").addEventListener("mouseover", animateWatering);
});


function animateWatering(){

    var imgs = ["-5.png", "-4.png", "-3.png", "-2.png", "-1.png", "1.png", "2.png", "3.png"]  
    let duration = 1
    let animationTarget = document.getElementById("submitButton")
    let img_folder_path = "static/img/konev_animation/"
    let index = imgs.length -1 ;
    var animateInterval = setInterval(()=>{
        if(index > 0){
            console.log(img_folder_path + imgs[index])
            animationTarget.src = img_folder_path + imgs[index]
            index -= 1
        }else{
            clearInterval(animateInterval)
        }
    }, (duration*1000)/imgs.length);

}
