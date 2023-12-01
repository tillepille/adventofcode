const fs = require('node:fs/promises');

async function main() {
    let numbers = []
    const file = await fs.open('./input.txt');
    for await (const line of file.readLines()) {
        const reversed = await reverseString(line)
        const first = await combiner(line)
        const second = await combiner(reversed)
        numbers.push(Number(first + second))
    }

    const result = numbers.reduce((total, current) => {return total + current}, 0);
    console.log("result is: " + result)
}

async function combiner(string) { 
  const rx = new RegExp("\\d");
  let arr = rx.exec(string);
  return arr[0]; 
}

async function reverseString(str) {
  return str.split("").reverse().join("");
}

main();
