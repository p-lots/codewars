const getGrade = (...args) => {
  const avg = args.reduce((acc, nxt) => acc + nxt, 0) / args.length;
  if (avg >= 90) {
    return "A";
  } else if (avg >= 80) {
    return "B";
  } else if (avg >= 70) {
    return "C";
  } else if (avg >= 60) {
    return "D";
  }
  return "F";
};
