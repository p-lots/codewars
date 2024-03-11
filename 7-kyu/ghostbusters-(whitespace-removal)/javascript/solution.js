const ghostBusters = (building) => {
  const noSpaces = building.split("").filter(elem => elem !== " ").join("");
  return noSpaces !== building ? noSpaces : "You just wanted my autograph didn't you?";
};
