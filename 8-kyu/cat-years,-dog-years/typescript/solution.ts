const petYears = (humanYears: number, factor: number): number => {
  return 15 * Number(humanYears >= 1) +
    9 * Number(humanYears >= 2) +
    (humanYears - 2) * factor * Number(humanYears >= 3);
}

export const humanYearsCatYearsDogYears = (humanYears: number): [number, number, number] => {
  const dogFactor = 5;
  const catFactor = 4;
  const dogYears = petYears(humanYears, dogFactor);
  const catYears = petYears(humanYears, catFactor);
  return [humanYears, catYears, dogYears];
};

