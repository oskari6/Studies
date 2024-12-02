if (object.x - object.width / 2 > right) {
  object.x = left - object.width / 2;
}
if (object.x + object.width / 2 < left) {
  object.x = right + object.width / 2;
}
if (object.y - object.height / 2 > bottom) {
  object.y = top - object.height / 2;
}
if (object.y + object.height / 2 < top) {
  object.x = bottom + object.height / 2;
}
