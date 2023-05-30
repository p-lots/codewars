const array = arr => {
  arr = arr.split(",");
  if (arr.length < 3) {
    return null;
  }
  return arr.slice(1, -1).join(" ");
};
