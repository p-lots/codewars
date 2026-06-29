const calcSeconds = (timestamp) => {
  const [ h, m, s ] = timestamp.split(":").map(Number);
  const totalSeconds = h * 3600 + m * 60 + s;
  return totalSeconds;
}

const evilCodeMedal = (userTime, ...places) => {
  const userSeconds = calcSeconds(userTime);
  const [ goldTime, silverTime, bronzeTime ] = places.map(calcSeconds);
  if (userSeconds < goldTime) {
    return "Gold";
  } else if (userSeconds < silverTime) {
    return "Silver";
  } else if (userSeconds < bronzeTime) {
    return "Bronze";
  }
  return "None";
};
