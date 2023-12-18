const zipWith = (fn, a0, a1) => {
  let first = a0;
  let second = a1;
  if (a0.length > a1.length) {
    first = first.slice(0, a1.length);
  } else if (a1.length > a0.length) {
    second = second.slice(0, a0.length);
  }
  const zipped = first.map((elem, idx) => fn(elem, second[idx]));
  return zipped;
};
