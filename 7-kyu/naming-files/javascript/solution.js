const nameFile = (fmt, nbr, start) => {
  if (nbr <= 0 || !Number.isInteger(nbr) || !Number.isInteger(start)) {
    return [];
  }
  else if (!fmt.includes("<index_no>")) {
    return Array(nbr).fill(fmt);
  }
  const ret = [];
  for (let i = start; i < start + nbr; i++) {
    const next = fmt.replaceAll("<index_no>", `${i}`);
    ret.push(next);
  }
  return ret;
}