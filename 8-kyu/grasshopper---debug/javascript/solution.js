const weatherInfo = temp => {
  const celsius = (temp - 32) * (5 / 9);
  return `${celsius} is ${celsius > 0 ? 'above ' : ''}freezing temperature`;
};
