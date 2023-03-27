const xMasTree = (n) => {
  let ret = [];
  for (let i = 1; i <= n; i++) {
    const underscores = "_".repeat(n - i);
    const center = "#".repeat(i * 2 - 1);
    ret.push(underscores + center + underscores);
  }
  const underTree = "_".repeat(n - 1) + "#" + "_".repeat(n - 1);
  for (let i = 0; i < 2; i++) {
    ret.push(underTree);
  }
  return ret;
};
