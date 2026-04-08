const match = (usefulness, months) => {
  const usefulnessSum = usefulness.reduce((acc, nxt) => acc + nxt, 0);
  const startingNeeds = 100;
  const decayRate = 0.15;
  const needs = (startingNeeds * (1 - decayRate) ** months);
  return usefulnessSum >= needs ? "Match!" : "No match!";
};
