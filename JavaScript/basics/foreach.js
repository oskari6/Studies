var arr = [1, 2 , 3];
//faster
for(var i = 0, len = arr.length; i < len; i++){
    console.log(arr[i]);
}

//foreach
//slower but shows as function calls in the callstack better for debugging
var arr = [1, 2, 3];
arr.forEach(function (element, i){
    console.log(element);
});