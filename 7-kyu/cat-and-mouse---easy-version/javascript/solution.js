const catMouse = x => {
  const catIndex = x.indexOf("C");
  const mouseIndex = x.indexOf("m");
  return Math.abs(catIndex - mouseIndex) <= 4 ? "Caught!" : "Escaped!";
}