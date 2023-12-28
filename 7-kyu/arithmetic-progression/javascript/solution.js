const arithmeticSequenceElements = (a, d, n) => {
	const progression = [];
  for (let i = 0; i < n; i++) {
    progression.push(a);
    a += d;
  }
  const joined = progression.join(", ");
  return joined;
};