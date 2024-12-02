// a2 = b2 + c2 - 2 * b * c * cos A
// b2 = a2 + c2 - 2 * a * c * cos B
// c2 = a2 + b2 - 2 * a * b * cos C

var A = Math.acos((b * b + c * c - a * a) / (2 * b * c))
var B  = Math.acos((a * a + c * c - b * b) / (2 * a * c))
var C = Math.acos((a * a + b * b - c * c) / (2 * a * b))