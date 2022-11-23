const lostSheep = (friday, saturday, total) => total - (friday.reduce((acc, nxt) => acc + nxt, 0) + saturday.reduce((acc, nxt) => acc + nxt, 0));
