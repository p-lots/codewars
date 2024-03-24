const capitalize = (s, arr) => {
  return s.split("")
    .map((ch, idx) => arr.includes(idx) ? ch.toUpperCase() : ch)
    .join("");
};
