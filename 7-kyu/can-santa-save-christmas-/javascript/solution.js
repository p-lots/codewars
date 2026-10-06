const calculateSeconds = timestamp => {
  const [hrs, mins, secs] = timestamp.split(":").map(Number);
  const hours = hrs * 60 * 60;
  const minutes = mins * 60;
  return hours + minutes + secs;
};

const determineTime = durations => {
  const secondsPerDay = 60 * 60 * 24;
  const totalSeconds = durations.map(calculateSeconds).reduce((acc, nxt) => acc + nxt, 0);
  return totalSeconds <= secondsPerDay;
};
