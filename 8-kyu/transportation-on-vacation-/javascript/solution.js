const rentalCarCost = days => {
  const total = days * 40;
  return days >= 7 ? total - 50 : days >= 3 ? total - 20 : total;
}