const sing = () => {
  let ret = [];
  for (let i = 99; i >= 0; i--) {
    if (i > 0) {
      const plural = i === 1 ? "" : "s";
      ret.push(`${i} bottle${plural} of beer on the wall, ${i} bottle${plural} of beer.`);
      ret.push(`Take one down and pass it around, ${i > 1 ? (i - 1) : "no more"} bottle${i - 1 !== 1 ? "s" : ""} of beer on the wall.`);
    } else {
      ret.push("No more bottles of beer on the wall, no more bottles of beer.");
      ret.push("Go to the store and buy some more, 99 bottles of beer on the wall.");
    }
  }
  return ret;
};
