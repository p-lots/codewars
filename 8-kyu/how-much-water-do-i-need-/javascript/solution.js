const howMuchWater = (water, load, clothes) => {
  if (load * 2 < clothes) {
    return "Too much clothes";
  }
  if (clothes < load) {
    return "Not enough clothes";
  }
  const neededWater = water * 1.1 ** Math.abs(load - clothes);
  return parseFloat(neededWater.toFixed(2));
};
