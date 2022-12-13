const cubeTimes = (times) => {
  const avg = times.sort((a, b) => a - b).slice(1, -1).reduce((acc, nxt) => acc + nxt, 0.0) / 3.0;
  return [Math.round(avg * 100) / 100, times[0]];
}