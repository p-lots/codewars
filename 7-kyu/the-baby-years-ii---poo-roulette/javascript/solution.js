const pooRoulette = p => {
  for (let i = 0; i < p.length; i++) {
    let scentCount = 0;
    const scentIdx = p[i].indexOf("~");
    if (scentIdx !== -1) {
      scentCount++;
      let isSameIdx = true;
      for (let j = i + 1; j < p.length; j++) {
        isSameIdx = scentIdx === p[j].indexOf("~");
        if (isSameIdx) {
          scentCount++;
        } else if (scentCount === 3 && p[j][scentIdx] === "B") {
          return "Get the wipes!";
        } else {
          scentCount = 0;
        }
      }
    }
  }
  for (let i = 0; i < p.length; i++) {
    const bIdx = p[i].indexOf("B");
    const scentIdx = p[i].indexOf("~");
    if (bIdx !== -1 && scentIdx !== -1) {
      const lowestIdx = Math.min(bIdx, scentIdx);
      const nextThree = p[i].slice(lowestIdx + 1, lowestIdx + 4).join("");
      if (nextThree.match(/~~[~B]/)) {
        return "You disgust me!";
      }
    }
  }
  return "Calm before the storm";
};
