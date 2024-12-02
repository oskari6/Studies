//substitute mouse.x, mouse.y, with the x, y point to rotate to
dx = mouseX - object.x;
dy = mouseY - object.y;
object.rotation = Math.atan2(dy, dx) * 180 / Math.PI; //radians to degrees