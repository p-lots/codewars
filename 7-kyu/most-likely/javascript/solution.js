const mostLikely = (prob1, prob2) => {
  const calcPercentage = (probability) => probability.split(":").map(elem => parseInt(elem)).reduce((acc, nxt) => acc / nxt);
  const firstPercentage = calcPercentage(prob1);
  const secondPercentage = calcPercentage(prob2);
  return firstPercentage > secondPercentage;
};
