var ax = (targetX - object.x)  *spring,
 ay = (targetY - object.y)  *spring;

 vx += ax;
 vy += ay;
 vx *= friction;
 vy *= friction;
 object.x += vx;
 object.y += vy;