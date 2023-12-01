const fs = require('node:fs/promises');

async function main() {
    let numbers = []
    const file = await fs.open('./input.txt');
    for await (const line of file.readLines()) {
        const reversed = await reverseString(line)
        const first = await extendedNumberFinder(line)
        const second = await extendedNumberFinder(reversed)
        numbers.push(Number(first + second))
    }

    const result = numbers.reduce((total, current) => {return total + current}, 0);
    console.log("result is: " + result)
}

// For Problem 1
async function numberFinder(string) { 
  const rx = new RegExp("\\d");
  let arr = rx.exec(string);
  return arr[0]; 
}

// For Problem 2
async function extendedNumberFinder(string) { 
  const rx = new RegExp("\\d");
  let arr = rx.exec(string);
  return arr[0]; 
}

async function reverseString(str) {
  return str.split("").reverse().join("");
}

main();
