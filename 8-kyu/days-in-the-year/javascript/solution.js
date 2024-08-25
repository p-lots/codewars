const yearDays = (year) => {
  const isLeapYear = year % 4 === 0 && !(year % 100 === 0) || year % 400 === 0;
  return `${year} has ${isLeapYear ? "366" : "365"} days`;
};
