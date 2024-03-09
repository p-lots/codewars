const trianglePerimeter = triangle => {
  const distance = (a, b) => Math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2);
  const perimeter = distance(triangle.a, triangle.b) + distance(triangle.b, triangle.c) + distance(triangle.c, triangle.a);
  return +perimeter.toFixed(6);
};
