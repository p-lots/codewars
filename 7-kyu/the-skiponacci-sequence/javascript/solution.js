function* genFibonacci() {
  yield 1;
  let a = 0;
  let b = 1;
  let c = a + b;
  while (true) {
    yield c;
    a = b;
    b = c;
    c = a + b;
  }
}

function skiponacci(n) {
  let i = 0;
  const sequence = [];
  const fib = genFibonacci();
  while (i < n) {
    const nextFib = fib.next().value;
    const toPush = i % 2 === 1 ? "skip" : nextFib;
    sequence.push(toPush);
    i++;
  }
  return sequence.join(" ");
}