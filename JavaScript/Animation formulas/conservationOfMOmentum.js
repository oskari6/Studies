var vxTotal = vx0 - vx1;
vx0 = ((ball0.mass - ball2.mass) * vx0 + 2 * ball2.mass * vx1) / (ball0.mass + ball1.mass);
vx1 = vxTotal + vx0;