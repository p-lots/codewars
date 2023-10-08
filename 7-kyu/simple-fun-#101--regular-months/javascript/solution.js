const regularMonths = currMonth => {
  const [mm, yyyy] = currMonth.split("-");
  let currDate = new Date(yyyy, mm);
  while (currDate.getUTCDay() !== 1) {
    currDate.setUTCMonth(currDate.getMonth() + 1);
  }
  let [nextRegMonth, nextRegYear] = [currDate.getMonth() + 1, currDate.getYear() + 1900];
  nextRegMonth = `${nextRegMonth}`.padStart(2, "0")
  return `${nextRegMonth}-${nextRegYear}`;
};
