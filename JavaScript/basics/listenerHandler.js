//element.addEventListener(type, handler[, useCapture]);
//third argument optional, affects how it bubbles dom tree, default false

//mousedown is important, difficult bug to track
canvas.addEventListener("mousedown", function(event){
    console.log("Mouse pressed on element!");
}, false);

//remove
// element.removeEventListener(type, handler[, useCapture]);