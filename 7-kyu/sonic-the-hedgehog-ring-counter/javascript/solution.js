const ringBank = (rings, monitors, giantrings, chaosEmeralds, sonicHit, sonicShield) => {
  if (sonicHit && !sonicShield) {
    return 0;
  }
  return rings + monitors * 10 + giantrings * (chaosEmeralds === 7 ? 50 : 0);
}