const titleToNumber = title => title.split("").reverse().map(digit => "ABCDEFGHIJKLMNOPQRSTUVWXYZ".indexOf(digit) + 1).reduce((acc, nxt, idx) => acc + 26 ** idx * nxt, 0);
