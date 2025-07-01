const add = (arr) => arr.map((_, idx, a) => a.slice(0, idx + 1).reduce((acc, nxt) => acc + nxt, 0));
