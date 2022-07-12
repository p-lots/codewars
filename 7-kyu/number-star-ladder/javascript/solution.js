const pattern = n => {
  let ret = [];
  for (let i = 0; i < n; i++) {
    ret.push(`1${i > 0 ? '*'.repeat(i) : ""}${i > 0 ? i + 1 : ""}`);
  }
  return ret.join('\n');
};
