//  object literal syntax extension

let temp1 = 1;
    temp2 = 2;
    
let obj = {
    temp1,
    temp2
}

console.log(temp1, "object literal");
console.log(temp2, "object literal");

/* rest parameter
* A rest parameter allows you to represent an indefinite number of arguments as an array.
* ...arr is rest parameter can take 0 - infinite args*/

function sum(a, ...arr) {
    let sum = a;
    for (let ar of arr) {
        sum += ar;
    }
    console.log(sum, "rest paramter");
}

sum(5,6,7,8,9);
sum(1);

/* spread operator
*  three dots (...), spread operator allows you to spread out elements of an 
*  iterable object such as an array,a map, or a set
*/
const arr2 = [1,2,3];
const arr3 = [...arr2,4,5,6];
console.log(arr3, "spread operator", ...arr3);
