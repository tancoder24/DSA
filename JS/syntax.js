/* 
* datatypes - 
* 1.null
* 2.undefined
* 3.boolean
* 4.number
* 5.NaN eg - 5/"tanmay" 
* 5.string 
* 6.object
* 7.symbol - let temp = Symbol("Tanmay Gupta")
*/

// variuable declaration
var a = 5, 
    b = 8;
let b = 6;
const c = 7;

// Array 
let arr = ["a", "b"];
console.log(arr.length);

// loops
for(let i=0; i<1; i++) {
    console.log("for-loop");
}
let i = 0;

do {
    console.log("do-while");
}while(i<0);

while(i<1) {
    console.log("while");
    i = 1;
}

for (let a of arr) {
    console.log("of "+a);
}

for (let a in arr) {
    console.log("in "+arr[a]);
}

// conditional operators

if(true) {
    console.log(true + " if-else");
} else {
    console.log(false);
}

const condition = true;
switch (condition) {
    case true: console.log(true + " switch case");
    break;
    case false: throw false;
    break;
    default: console.log("Nothing")
}

const ans  = (5>4) ? console.log(true + " terniary operator"): console.log(false);

// function declaration
function add(a,b) {
    console.log(a+b);
}

const add_new = (a,b) => {
    console.log(a+b);
}

add(a,b);
add_new(a,b);