const cubeOdd = arr => arr.every(elem => Number.isInteger(elem)) ? arr.map(n => n ** 3).filter(n => n % 2 !== 0).reduce((acc, nxt) => acc + nxt, 0) : undefined;
