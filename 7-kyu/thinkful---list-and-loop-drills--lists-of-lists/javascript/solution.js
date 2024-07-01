const processData = data => data.reduce((acc, nxt) => acc * (nxt[0] - nxt[1]), 1);
