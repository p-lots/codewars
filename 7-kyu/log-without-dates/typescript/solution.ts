export const checkLogs = (log: string[]): number => {
  if (log.length === 0) {
    return 0;
  }
  let days = 1;
  for (let i = 1; i < log.length; i++) {
    if (log[i - 1] >= log[i]) {
      days++;
    }
  }
  return days;
};
