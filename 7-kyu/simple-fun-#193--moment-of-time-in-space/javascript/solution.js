const momentOfTimeInSpace = moment => {
  const time = moment.split("")
    .reduce((acc, nxt) => /[1-9]/.test(nxt) ? acc + Number.parseInt(nxt) : acc, 0);
  const space = moment.split("")
    .reduce((acc, nxt) => /[^1-9]/.test(nxt) ? acc + 1 : acc, 0);
  return [time < space, time === space, time > space];
};
