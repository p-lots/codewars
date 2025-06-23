function stonePick(arr) {
  const cobble = arr.filter((elem) => elem === "Cobblestone").length;
  const sticks = arr.filter((elem) => elem === "Sticks").length + arr.filter((elem) => elem === "Wood").length * 4;
  return Math.min(Math.floor(cobble / 3), Math.floor(sticks / 2));
}