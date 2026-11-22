const findDeletedNumber = (arr, mixArr) => arr.reduce((acc, nxt) => acc + nxt, 0) - mixArr.reduce((acc, nxt) => acc + nxt, 0);
