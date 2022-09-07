const all = (arr, fun) => {
  for (const elem of arr) {
    if (!fun(elem)) {
      return false;
    }
  }
  return true;
};