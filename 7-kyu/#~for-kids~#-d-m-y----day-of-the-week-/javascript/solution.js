const dayOfTheWeek = date => {
  let [day, month, year] = date.split("/");
  month = (parseInt(month) - 1).toString();
  const dateObj = new Date(year, month, day);
  const dayOfWeek = dateObj.getDay();
  return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][dayOfWeek];
};
