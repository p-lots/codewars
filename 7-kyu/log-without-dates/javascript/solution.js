const checkLogs = log => {
  if (log.length === 0) {
    return 0;
  }
  let daysInLog = 1;
  for (let i = 1; i < log.length; i++) {
    if (log[i - 1] >= log[i]) {
      daysInLog++;
    }
  }
  return daysInLog;
}