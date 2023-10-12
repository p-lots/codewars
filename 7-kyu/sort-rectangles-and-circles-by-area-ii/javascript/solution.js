const getArea = shape => Array.isArray(shape) ? shape[0] * shape[1] : Math.PI * shape * shape;

const sortByArea = array => {
  const arrayCopy = JSON.parse(JSON.stringify(array));
  return arrayCopy.sort((a, b) => getArea(a) - getArea(b));
};
