const neutralise = (s1, s2) => {
  const neutralised = s1.split("")
    .map((item, idx) => item !== s2[idx] ? "0" : item)
    .join("");
  return neutralised;
};
