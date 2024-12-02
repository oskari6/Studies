let buffer = new ArrayBuffer(16);
let view = new DataView(buffer);

view.setInt8(0, 127);
view.setUint8(1, 255);
view.setInt16(2, 32767, true);
view.setFloat32(4, 3.14, true);

console.log(view.getInt8(0));
console.log(view.getUint8(1));
console.log(view.getInt16(2, true));
console.log(view.getFLoat32(4, true));
