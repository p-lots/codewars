const to24hourtime = (hour, minute, period) => {
  // hour will always range from 1 to 12 (inclusive)
  // minute will always range from 0 to 59 (inclusive)
  // period will always be either "am" or "pm"
  let hour24 = hour;
  if (period === "am") {
    hour24 %= 12;
  } else if (hour < 12) {
    hour24 += 12;
  }
  return `${hour24.toString().padStart(2, "0")}${minute.toString().padStart(2, "0")}`;
};
