const capitals = word => {
	const capitalIdxs = [];
  for (let i = 0; i < word.length; i++) {
    if (word[i].toUpperCase() === word[i]) {
      capitalIdxs.push(i);
    }
  }
  return capitalIdxs;
};