const getSlope = (p1, p2) => {
  // Return the slope of the line through p1 and p2
  const rise = p2[1] - p1[1];
  const run = p2[0] - p1[0];
  return run === 0 ? null : rise / run;
};
