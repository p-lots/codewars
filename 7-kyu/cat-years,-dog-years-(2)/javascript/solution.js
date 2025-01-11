const calcPetAge = (petYears, ageFactor) => {
  if (petYears < 15) {
    return 0;
  }
  petYears -= 15;
  if (petYears < 9) {
    return 1;
  }
  return Math.floor(2 + (petYears - 9) / ageFactor);
}

const ownedCatAndDog = (catYears, dogYears) => {
  const catAgeFactor = 4;
  const dogAgeFactor = 5;
  const catAge = calcPetAge(catYears, catAgeFactor);
  const dogAge = calcPetAge(dogYears, dogAgeFactor);
  return [catAge, dogAge];
};
