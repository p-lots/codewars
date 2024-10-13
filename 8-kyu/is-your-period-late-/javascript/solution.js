const periodIsLate = (last, today, cycleLength) => {
  const MILLISECONDS_PER_DAY = 24 * 60 * 60 * 1000;
  return last.getTime() + cycleLength * MILLISECONDS_PER_DAY < today.getTime();
}