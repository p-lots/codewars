const solve = arr => arr.filter((elem, idx, a) => a.slice(idx + 1).every(n => elem > n));
