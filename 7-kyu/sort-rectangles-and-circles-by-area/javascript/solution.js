const getArea = measurement => typeof measurement === 'object' ? measurement[0] * measurement[1] : Math.PI * measurement * measurement;

const sortByArea = array => {
  return array.map(elem => Math.round(getArea(elem) * 100) / 100).sort((a, b) => a - b);
};
