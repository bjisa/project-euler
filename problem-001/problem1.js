// Project Euler
// Problem 1

function* getMultiplesOf(upperBound, terms) {
  let current = 1;
  while (current < upperBound) {
    if (terms.some((term) => current % term === 0)) {
      yield current;
    }
    current++;
  }
}

const multiples = getMultiplesOf(1000, [3, 5]);

let sumOfMultiples = 0;
let currentMultiple = multiples.next().value;

while (currentMultiple) {
  sumOfMultiples += currentMultiple;
  currentMultiple = multiples.next().value;
}

console.log(sumOfMultiples);