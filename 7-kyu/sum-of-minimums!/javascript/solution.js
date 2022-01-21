const sumOfMinimums = (arr) => {
  return arr.map((subArr) => Math.min(...subArr)).reduce((acc, next) => acc + next, 0);
};