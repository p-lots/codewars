const toDayOfYear = (arr) => {
  const newArr = [arr[2], (arr[1] - 1), arr[0]];
  const jan1Date = new Date(Date.UTC(newArr[0], 0, 1));
  const arrDate = new Date(Date.UTC(...newArr));
  return (arrDate - jan1Date) / (1000 * 60 * 60 * 24) + 1;
};
