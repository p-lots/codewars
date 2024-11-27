const isOpposite = (s1, s2) => {
  if (!s1 || !s2) {
    return false;
  }
  const oppositeCase = [...s2].map((ch) => ch.toLowerCase() === ch ? ch.toUpperCase() : ch.toLowerCase()).join("");
  return s1 === oppositeCase;
};
