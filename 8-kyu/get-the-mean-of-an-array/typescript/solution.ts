export const getAverage = (marks: number[]): number => {
  //TODO : calculate the downwar rounded average of the marks array
  const avg = marks.reduce((acc, nxt) => acc + nxt, 0) / marks.length;
  return Math.floor(avg);
}