const sortDict = dict => {
  let unsortedDict = [];
  for (const pair of Object.entries(dict)) {
    const [key, val] = pair;
    if (parseInt(key)) {
      unsortedDict.push([parseInt(key), val]);
    } else {
      unsortedDict.push(pair);
    }
  }
  return unsortedDict.sort((a, b) => b[1] - a[1]);
};
