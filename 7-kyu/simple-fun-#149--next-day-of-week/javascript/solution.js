const nextDayOfWeek = (currentDay, availableWeekDays) => {
  const availableDays = availableWeekDays.toString(2).padStart(8, '0').split("").reverse().join("");
  let idx = currentDay % availableDays.length;
  while (availableDays[idx] !== '1') {
    idx++;
    idx = idx % availableDays.length;
  }
  return idx + 1;
};
