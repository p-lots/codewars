const findOddNames = list => list.filter(entry => entry.firstName.split("").map(ch => ch.charCodeAt(0)).reduce((acc, nxt) => acc + nxt, 0) % 2 === 1);
