scale = fl / (fl + zpos);
objects.scaleX = object.scaleY = scale;
objects.alpha = scale; //optional
object.x = vanishingPointX + xpos * scale;
object.y = vanishingPointY + ypos * scale;