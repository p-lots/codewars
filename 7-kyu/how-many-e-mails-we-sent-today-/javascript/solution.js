const getPercentage = (sent, limit = 1000) => {
  if (sent === 0) {
    return "No e-mails sent";
  } else if (sent >= limit) {
    return "Daily limit is reached";
  }
  const pct = Math.floor(sent / limit * 100);
  return `${pct}%`;
};
