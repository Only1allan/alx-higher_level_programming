#!/usr/bin/node
const arg =  process.argv.slice(2)[0];
if (arg === undefined){
    console.log("Missing number of occurences");
}
else {
    for (let i = 0; i < arg; i++){
        console.log("C is fun");
    }
}
