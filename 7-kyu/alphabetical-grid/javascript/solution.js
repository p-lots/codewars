const grid = N => {
  if (N < 0) {
    return null;
  }
  let ret = [];
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  for (let i = 0; i < N; i++) {
    let line = [];
    for (let j = i; j < N + i; j++) {
      line.push(alphabet[j % alphabet.length]);
    }
    ret.push(line.join(' '));
  }
  return ret.join('\n');
};
