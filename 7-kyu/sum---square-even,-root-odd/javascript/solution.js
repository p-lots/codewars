const sumSquareEvenRootOdd = ns => Math.round(ns.map(n => (n % 2 === 0 ? n ** 2 : n ** 0.5)).reduce((acc, nxt) => acc + nxt, 0) * 100) / 100;
