const countBits = n => n.toString(2).split("").reduce((acc, nxt) => nxt === "1" ? acc + 1 : acc, 0);
