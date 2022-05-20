const correctness = (bobsDecisions, expertDecisions) => {
  let ret = 0;
  for (let i = 0; i < bobsDecisions.length; i++) {
    if (bobsDecisions[i] === expertDecisions[i]) {
      ret += 1;
    } else if (bobsDecisions[i] === '?' || expertDecisions[i] === '?') {
      ret += 0.5;
    }
  }
  return ret;
};