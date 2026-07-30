const convert = time => {
  const hh = `${time.getHours()}`.padStart(2, "0");
  const mm = `${time.getMinutes()}`.padStart(2, "0");
  const ss = `${time.getSeconds()}`.padStart(2, "0");
  const ms = `${time.getMilliseconds()}`.padStart(3, "0");
  return `${hh}:${mm}:${ss},${ms}`;
};
