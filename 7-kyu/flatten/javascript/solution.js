const flatten = array => {
  let flattened = [];
  array.forEach(element => {
    if (Array.isArray(element)) {
      element.forEach(sub => {
        flattened.push(sub);
      });
    } else {
      flattened.push(element);
    }
  });
  return flattened;
};
