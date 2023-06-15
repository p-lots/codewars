const feast = (beast, dish) => {
  const beastLastIdx = beast.length - 1;
  const dishLastIdx = dish.length - 1;
  return beast[0] === dish[0] && beast[beastLastIdx] === dish[dishLastIdx];
};
