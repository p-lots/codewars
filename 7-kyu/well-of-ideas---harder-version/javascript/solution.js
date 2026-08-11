const well = x => {
  const goodCount = x.map((subarr) => subarr.filter((elem) => typeof elem === "string" && /good/i.test(elem)).length).reduce((acc, nxt) => acc + nxt, 0);
  if (goodCount > 2) {
    return "I smell a series!";
  } else if (goodCount > 0) {
    return "Publish!";
  }
  return "Fail!";
};
