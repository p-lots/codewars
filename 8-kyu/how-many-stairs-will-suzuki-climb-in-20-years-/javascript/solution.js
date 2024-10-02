const stairsIn20 = (s) => s.reduce((acc, row) => acc + row.reduce((accum, nxt) => accum + nxt, 0), 0) * 20;
