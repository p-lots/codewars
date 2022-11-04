const bump = x => {
  let bumpCount = [...x].filter(elem => elem === "n").length;
  return bumpCount > 15 ? "Car Dead" : "Woohoo!";
}