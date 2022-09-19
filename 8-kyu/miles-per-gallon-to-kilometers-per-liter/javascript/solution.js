const converter = mpg => {
  const GAL_IN_L = 1.609344;
  const MILES_IN_KM = 4.54609188;
  return Math.round(mpg * GAL_IN_L / MILES_IN_KM * 100) / 100;
};
