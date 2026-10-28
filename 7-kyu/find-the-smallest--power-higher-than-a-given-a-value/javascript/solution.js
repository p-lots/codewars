const findNextPower = (val, pow_) => {
  const nextPower = Math.pow((Math.floor(Math.pow(val, (1 / pow_))) + 1), pow_);
  if (nextPower === val) return findNextPower(val + 1, pow_);
  return nextPower;
};
