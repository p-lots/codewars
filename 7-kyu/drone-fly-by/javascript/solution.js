const flyBy = (lamps, drone) => {
  const lampsLen = lamps.length;
  const droneLen = drone.length;
  const oRepeat = droneLen > lampsLen ? droneLen - 1 : droneLen;
  const xRepeat = Math.max(Math.min(lampsLen - droneLen, lampsLen), 0);
  return `${'o'.repeat(oRepeat)}${'x'.repeat(xRepeat)}`;
};
