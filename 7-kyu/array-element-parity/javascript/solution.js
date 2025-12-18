const solve = (arr) => [...new Set(arr)].reduce((acc, nxt) => acc + nxt, 0);
