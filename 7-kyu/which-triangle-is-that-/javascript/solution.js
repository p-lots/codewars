const typeOfTriangle = (sideA, sideB, sideC) => {
  if (typeof sideA !== "number" || typeof sideB !== "number" || typeof sideC !== "number") {
    return "Not a valid triangle";
  }
  const sides = [sideA, sideB, sideC].sort((a, b) => a - b);
  if (sides[0] + sides[1] > sides[2]) {
    if (sideA === sideB && sideB === sideC) {
      return "Equilateral";
    } else if (sideA === sideB || sideB === sideC || sideA === sideC) {
      return "Isosceles";
    }
    return "Scalene";
  }
  return "Not a valid triangle";
}