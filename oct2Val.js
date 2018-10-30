function d2o(val){
    var e = 0;
    var newStr = "";
    while(val/(Math.pow(8,(e+1))) > 1){
        console.log("Math.pow(8,(e+1) = ", Math.pow(8,(e+1)))
        console.log("e = ", e)
        console.log("val/(Math.pow(8,(e+1))) = ", val/(Math.pow(8,(e+1))));
        e++;
    }
    while(e >= 0){
        console.log("start: digit = ",digit," rem = ",rem," newStr = ",newStr)
        var digit = Math.trunc(val/(Math.pow(8,e)));
        var rem = val % Math.pow(8, e);
        newStr = newStr+digit;
        console.log("end: digit = ",digit," rem = ",rem," newStr = ",newStr)
        e--;
        val = rem;
    }
    return newStr;

}

// console.log("d2o(1): "+d2o(1));
// console.log("d2o(10): "+d2o(10));
// console.log("d2o(65): "+d2o(65));
var x = d2o(9947372);
console.log("x = "+x);