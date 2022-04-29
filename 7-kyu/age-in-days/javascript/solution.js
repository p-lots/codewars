const ageInDays = (year, month, day) =>{
  const today = new Date();
  const todayUTC = Date.UTC(today.getFullYear(), today.getMonth(), today.getDate());
  const birthdayUTC = Date.UTC(year, month - 1, day);
  const daysOld = Math.floor((todayUTC - birthdayUTC) / (1000 * 60 * 60 * 24));
  return `You are ${daysOld} days old`;
};
