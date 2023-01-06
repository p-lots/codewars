const tripleX = (str) => {
  const firstXIndex = str.indexOf("x");
  if (firstXIndex === -1) {
    return false;
  }
  return str.substr(firstXIndex, 3) === "xxx";
};
