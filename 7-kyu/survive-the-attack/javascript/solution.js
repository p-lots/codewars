const hasSurvived = (attackers, defenders) => {
  if (attackers.length === 0 && defenders.length === 0) {
    return true;
  } else if (defenders.length === 0) {
    return false;
  } else if (attackers.length === 0) {
    return true;
  }
  const atkTotal = attackers.reduce((acc, nxt) => acc + nxt, 0);
  const defTotal = defenders.reduce((acc, nxt) => acc + nxt, 0);
  while (attackers.length < defenders.length) {
    attackers.push(-1);
  }
  while (defenders.length < attackers.length) {
    defenders.push(-1);
  }
  let ret = 0;
  for (let i = 0; i < attackers.length; i++) {
    if (attackers[i] > defenders[i]) {
      ret--;
    } else if (defenders[i] > attackers[i]) {
      ret++;
    }
  }
  if (ret === 0) {
    if (atkTotal === defTotal) {
      return true;
    }
    return atkTotal < defTotal;
  }
  return ret > 0;
};
