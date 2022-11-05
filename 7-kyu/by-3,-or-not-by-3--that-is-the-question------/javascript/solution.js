const divisibleByThree = str => str.split("").map(elem => parseInt(elem)).reduce((acc, nxt) => acc + nxt, 0) % 3 === 0;
