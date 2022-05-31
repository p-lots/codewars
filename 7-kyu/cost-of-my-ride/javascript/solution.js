const insurance = (age, size, numOfDays) => {
  const ageCharge = age < 25 ? 10 : 0;
  let dailyCharge = 50 + ageCharge;
  switch (size) {
      case 'economy':
      break;
      case 'medium':
      dailyCharge += 10;
      break;
      default:
      dailyCharge += 15;
  }
  return Math.max(numOfDays, 0) * dailyCharge;
};