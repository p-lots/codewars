const cookingTime = (neededPower, minutes, seconds, power) => {
  const actualNeededPower = Number(neededPower.slice(0, -1));
  const actualPower = Number(power.slice(0, -1));
  const totalSeconds = minutes * 60 + seconds;
  const neededSeconds = Math.ceil(totalSeconds * (actualNeededPower / actualPower));
  const actualMinutes = Math.floor(neededSeconds / 60);
  const actualSeconds = neededSeconds % 60;
  return `${actualMinutes} minutes ${actualSeconds} seconds`;
};
