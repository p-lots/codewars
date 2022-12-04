const XO = str => {
  str = str.toLowerCase();
  return str.split("").filter(elem => elem === "x").length === str.split("").filter(elem => elem === "o").length;
};
