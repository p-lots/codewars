const shadesOfGrey = (n) => {
  let ret = [];
  for (let i = 1; i < 255; i++) {
    const toPush = `${i.toString(16).padStart(2, '0')}`;
    ret.push(`#${toPush.repeat(3)}`);
  }
  return ret.slice(0, Math.min(Math.max(n, 0), 254));
};
