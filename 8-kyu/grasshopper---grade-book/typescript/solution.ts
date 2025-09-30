export function getGrade(...args: number[]): string {
  const average = args.reduce((acc, nxt) => acc + nxt, 0) / arguments.length;
  if (average >= 0 && average < 60) {
    return "F";
  } else if (average < 70) {
    return "D";
  } else if (average < 80) {
    return "C";
  } else if (average < 90) {
    return "B";
  }
  return "A";
}