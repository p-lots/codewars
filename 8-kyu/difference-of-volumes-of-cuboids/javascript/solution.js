const findDifference = (a, b) => Math.abs(a.reduce((acc, nxt) => acc * nxt, 1) - b.reduce((acc, nxt) => acc * nxt, 1));