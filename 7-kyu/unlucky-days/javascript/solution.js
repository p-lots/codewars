const unluckyDays = year => {
  let dayCount = 0;
  for (let i = 0; i < 12; i++) {
    const date = new Date(year, i, 13);
    if (date.getDay() === 5) {
      dayCount++;
    }
  }
  return dayCount;
};