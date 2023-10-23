const dropWhile = (arr, pred) => {
  const span = (array, predicate) => {
    let i = 0;
    while (i < array.length) {
      if (!predicate(array[i])) {
        break;
      }
      i++;
    }
    return [array.slice(i), array.slice(0, i)];
  };
  return span(arr, pred)[0];
};
