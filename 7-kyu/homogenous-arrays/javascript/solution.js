const filterHomogenous = arrays => {
  return arrays.filter(arr => arr.length > 0 && arr.every((elem, _, a) => typeof elem === typeof a[0]));
}