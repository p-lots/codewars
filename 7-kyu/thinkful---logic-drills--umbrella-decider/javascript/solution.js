const takeUmbrella = (weather, chance) => {
  if (weather === "sunny") {
    return chance - 0.5 > 0.00001;
  }
  else if (weather === "cloudy") {
    return chance - 0.2 > 0.00001;
  }
  return true;
};
