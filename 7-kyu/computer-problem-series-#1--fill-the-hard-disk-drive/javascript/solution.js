const save = (sizes, hd) => {
  if (!sizes) {
    return 0;
  }
  if (sizes[0] > hd) {
    return 0;
  }
  let ret = 0;
  let sum = 0;
  while (sizes.length > 0 && sizes[0] + sum <= hd) {
    sum += sizes.shift();
    ret++;
    if (sizes.length > 0 && sizes[0] + sum > hd) {
      break;
    }
  }
  return ret;
};
