let canvas = document.getElementById('myCanvas');
let ctx = canvas.getContext("2d");
let mousePressed = false;

canvas.addEventListener("mousedown", function (e) {
    mousePressed = true;
    Draw(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, false);
});

canvas.addEventListener("mouseup", function (e) {
    mousePressed = false;
});

canvas.addEventListener("mouseleave", function (e) {
    mousePressed = false;
});


canvas.addEventListener("mousemove", function (e) {
    if (mousePressed) {
        Draw(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
    }
});


function Draw(x, y, isDown) {
    if (isDown) {
        ctx.beginPath();
        ctx.strokeStyle = "#000000";
        ctx.lineWidth = 20;
        ctx.lineJoin = "round";
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.stroke();
    }
    lastX = x;
    lastY = y;

    document.getElementById("canvas-data").value = document.getElementById("myCanvas").toDataURL("image/png").replace(/^data:image\/(png|jpg);base64,/, "");
}


function clearArea() {
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);

}