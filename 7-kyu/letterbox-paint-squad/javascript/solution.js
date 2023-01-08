const paintLetterboxes = (start, end) => {
  let ret = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  for (let i = start; i <= end; i++) {
    const iStr = i.toString();
    iStr.split("").forEach(elem => ret[parseInt(elem)] += 1);
  }
  return ret;
};
