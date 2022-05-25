const getAverageAge = (list) => Math.round(list.reduce((acc, nxt) => acc + nxt.age, 0) / list.length);
