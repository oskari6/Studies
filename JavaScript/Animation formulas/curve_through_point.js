//xt, yt is the point you want to draw through
//x0, y0 and x2, y2 are the end points of the curve
x1 = xt * 2 - (x0 + x2) / 2;
y1 = yt * 2 - (y0 + y2) / 2;

AudioContext.moveTo(x0, y0);
AudioContext.quadraticCurveTo(x1, y1, x2, y2);