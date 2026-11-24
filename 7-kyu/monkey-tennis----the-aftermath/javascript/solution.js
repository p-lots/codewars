const ballCollector = (detritus) => {
  const BALLWEIGHT = 58;
  const totalBalls = detritus.filter((itemWeight) => itemWeight === BALLWEIGHT).length;
  return { weight: totalBalls * BALLWEIGHT };
};
