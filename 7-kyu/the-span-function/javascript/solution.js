const span = (arr, predicate) => {
  if (!predicate(arr[0])) {
    return [[], arr];
  }
  let first = [];
  let second = [];
  let i = 0;
  let foundFirstTrue = false;
  while (i < arr.length) {
    if (!foundFirstTrue) {
      foundFirstTrue = true;
      while (i < arr.length && predicate(arr[i])) {
        first.push(arr[i]);
        i++;
      }
    }
    if (i < arr.length && foundFirstTrue) {
      second.push(arr[i]);
    }
    i++;
  }
  return [first, second];
};