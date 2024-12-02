MyObject.prototype.hello = function(){
    console.log("Hello, " + this.name);
};

objA.hello();

var objB = new MyObject("Inspired Coder");

objB.hello();