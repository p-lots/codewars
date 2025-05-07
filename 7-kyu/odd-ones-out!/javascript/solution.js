const oddOnesOut = nums => nums.filter((num, _, arr) => arr.filter(n => n === num).length % 2 === 0);
