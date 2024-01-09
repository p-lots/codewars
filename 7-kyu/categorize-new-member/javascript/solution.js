const openOrSenior = data => {
  const categorizer = elem => {
    const [age, handicap] = elem;
    return age >= 55 && handicap > 7 ? "Senior" : "Open";
  }
  return data.map(categorizer);
};
