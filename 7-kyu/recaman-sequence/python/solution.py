const recaman = n => {
  const seq = [0];
  let i = 1;
  let next = 1;
  while (seq.length <= n) {
    seq.push(next);
    if (seq.length > n) {
      break;
    }
    const last = seq.at(-1);
    i++;
    if (last - i > 0 && !seq.includes(last - i)) {
      next = last - i;
    } else {
      next = last + i;
    }
  }
  return seq.at(-1);
}