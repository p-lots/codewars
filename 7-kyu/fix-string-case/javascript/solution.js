const solve = s => {
  const upperCount = s.split("").filter(elem => elem === elem.toUpperCase()).length;
  const lowerCount = s.split("").filter(elem => elem === elem.toLowerCase()).length;
  return upperCount > lowerCount ? s.toUpperCase() : s.toLowerCase();
};