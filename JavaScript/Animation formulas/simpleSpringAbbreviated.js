vx += (targetX - object.x) * spring;
vy += (targetY - object.y) * spring;
vx *= friction;
vy *= friction;
object.x += vx;
object.y += vy;