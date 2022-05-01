const helpJesse = array => {
  let ret = [];
  for (const inst of array) {
    let s = `Pour ${inst.amount} mL of ${inst.solution} into a ${inst.instrument}`;
    if (inst.note) {
      s += ` (${inst.note})`;
    }
    ret.push(s);
  }
  return ret;
}