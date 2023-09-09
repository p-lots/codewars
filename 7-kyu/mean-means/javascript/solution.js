const geo_mean = (nums, arith_mean) => {
  const missingNumber = arith_mean * (nums.length + 1) - nums.reduce((acc, nxt) => acc + nxt, 0);
  nums.push(missingNumber);
  const geomMean = nums.reduce((acc, nxt) => acc * nxt, 1) ** (1 / nums.length);
  return geomMean;
}