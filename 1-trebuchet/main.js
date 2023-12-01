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
  const stringNumbers = [
    "one|eno",
    "two|owt",
    "three|eerht",
    "four|ruof",
    "five|evif",
    "six|xis",
    "seven|neves",
    "eight|thgie",
    "nine|enin",
    "\\d"
  ]

  let results = []
  for (let index = 0; index < stringNumbers.length; index++) {
    const element = stringNumbers[index]
    const rx = new RegExp(element)
    const singleResult = rx.exec(string)
    if (singleResult != null) {results.push(singleResult)}
  }

  results.sort(function(a, b){return a.index - b.index});
  const firstNumber = results[0]
  return transformToNumberString(firstNumber[0])
}

async function transformToNumberString (str) {
  const rx = new RegExp("\\d")
  if (rx.test(str)) {
    return str
  } else {
   switch (str) {
    case "one":
      return "1"
    case "two":
      return "2"
    case "three":
      return "3"
    case "four":
      return "4"
    case "five":
      return "5"
    case "six":
      return "6"
    case "seven":
      return "7"
    case "eight":
      return "8"
    case "nine":
      return "9"
   
    default:
      return transformToNumberString(await reverseString(str))
   } 
  }
}
async function reverseString(str) {
  return str.split("").reverse().join("");
}

main();
