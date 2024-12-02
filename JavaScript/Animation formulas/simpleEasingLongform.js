var dx = targetX - object.x,
dy = targertY - object.y;

vx = dx * easing;
vy = dy * easing;
object.x += vx;
object.y += vy;