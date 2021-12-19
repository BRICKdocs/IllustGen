const canvas = document.getElementById("sketch");
const ctx = canvas.getContext("2d");

canvas.width = 400;
canvas.height = 600;

ctx.strokeStyle = "black";
ctx.lineWidth = 1.5;

let painting = false;

function startPainting() {
    painting=true;
}
function stopPainting(event) {
    painting=false;
}

function onMouseMove(event) {
    const x = event.offsetX;
    const y = event.offsetY;
    if(!painting) {
        ctx.beginPath();
        ctx.moveTo(x, y);
    }
    else {
        ctx.lineTo(x, y);
        ctx.stroke();
    }
}

if (canvas) {
    canvas.addEventListener("mousemove", onMouseMove);
    canvas.addEventListener("mousedown", startPainting);
    canvas.addEventListener("mouseup", stopPainting);
    canvas.addEventListener("mouseleave", stopPainting);
}