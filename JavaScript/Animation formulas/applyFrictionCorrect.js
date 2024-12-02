speed = Math.sqrt(vx * vx + vy * vy);
angle = Math.atan2(vy , vx);

if(speed > friction){
    speed -= friction;
}else{
    speed = 0;
}

vx = Math.cos(angle) * speed;
vy = Math.sin(angle) * speed;