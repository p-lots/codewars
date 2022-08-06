const sortBytes = uint32 => {
  const bin = uint32.toString(2).padStart(32, '0');
  const first = bin.slice(0, 8);
  const second = bin.slice(8, 16);
  const third = bin.slice(16, 24);
  const fourth = bin.slice(24, 32);
  const ret = [first, second, third, fourth].sort((a, b) => parseInt(b, 2) - parseInt(a, 2));
  return parseInt(ret.join(""), 2);
};