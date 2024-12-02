vx += (targetX - object.x) * spring;
vy += (targetY - object.y) * spring;
object.x += (vx *= friction);
object.y += (vy *= friction);