var dx = objects.x - fixedX,
dy = object.y - fixedY,
angle = Math.atan2(dy ,dx),
targetX = fixedX + Math.cos(angle) * springLength;
targetY = fixedY + Math.sin(angle) * springLength;

//spring to targetX, targetY as above