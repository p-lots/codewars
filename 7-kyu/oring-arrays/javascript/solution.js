const orArrays = (arr1, arr2, filler = 0) => {
  let longer, shorter;
  if (arr1.length > arr2.length) {
    longer = arr1;
    shorter = arr2;
  } else {
    longer = arr2;
    shorter = arr1;
  }
  const ordArray = [];
  for (let i = 0; i < longer.length; i++) {
    const ordVal = longer[i] | (i < shorter.length ? shorter[i] : filler);
    ordArray.push(ordVal);
  }
  return ordArray;
};
