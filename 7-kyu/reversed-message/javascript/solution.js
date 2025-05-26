const reverseMessage = str => {
  if (str.length === 0) {
    return str;
  }
  return str.split("")
    .reverse()
    .join("")
    .toLowerCase()
    .split(" ")
    .map(word => word[0].toUpperCase() + word.slice(1))
    .join(" ");
};
