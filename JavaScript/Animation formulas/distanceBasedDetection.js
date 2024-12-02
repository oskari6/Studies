//starting with objectA and objectB
//if using an object without a radius property
//you can use width ot height divided by 2
var dx = objectB.x - objectA.x,
dy = objectB.y -objectA.y,
dist = Math.sqrt(dx * dx + dy * dy);

if(dist < objectA.radius + objectB.radius){
    //handle collision
}