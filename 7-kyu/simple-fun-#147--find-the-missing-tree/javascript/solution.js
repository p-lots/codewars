const findTheMissingTree = (trees) => {
  const counts = {};
  for (const tree of trees) {
    if (!counts.hasOwnProperty(tree)) {
      counts[tree] = 1;
    } else {
      counts[tree]++;
    }
  }
  const biggest = Math.max(...Object.values(counts));
  return trees.find((tree) => counts[tree] === biggest - 1);
};
