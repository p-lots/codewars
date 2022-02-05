'use strict';

const humanYearsCatYearsDogYears = humanYears => {
  const calcPetYears = (humanYears, factor) => 15 * (humanYears >= 1) + 9 * (humanYears >= 2) + (humanYears - 2) * factor * (humanYears >= 3);
  const catFactor = 4;
  const dogFactor = 5;
  return [humanYears,calcPetYears(humanYears, catFactor),calcPetYears(humanYears, dogFactor)];
}
