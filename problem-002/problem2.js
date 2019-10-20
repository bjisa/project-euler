// Project Euler
// Problem 2

function* getFibonacci() {
  let n1 = 1;
  yield n1;
  let n2 = 2;
  yield n2;

  while (true) {
    let n3 = n1 + n2;
      yield n3;
    n1 = n2;
    n2 = n3;
  }
}

const generator = getFibonacci();
let sum = 0;
let fibonacciNumber = 0;

while (fibonacciNumber < 4000000) {
  fibonacciNumber = generator.next().value;
  if (fibonacciNumber % 2 === 0)
    sum += fibonacciNumber;
}

console.log(sum);