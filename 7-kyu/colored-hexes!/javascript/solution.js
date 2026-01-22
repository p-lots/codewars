const hexColor = codes => {
  if (codes.length === 0) {
    return "black";
  }
  const [red, green, blue] = codes.split(" ").map(n => Number.parseInt(n, 10));
  if (red === green && green === blue) {
    return red === 0 ? "black" : "white";
  }
  if (red === blue && red > green) {
    return "magenta";
  } else if (green === red && green > blue) {
    return "yellow";
  } else if (blue === green && blue > red) {
    return "cyan";
  }
  const greatest = Math.max(red, green, blue);
  if (greatest === red) {
    return "red";
  } else if (greatest === green) {
    return "green";
  }
  return "blue";
};
