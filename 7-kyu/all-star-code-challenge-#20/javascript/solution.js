const addArrays = (array1, array2) => {
  if (array1.length !== array2.length) {
    throw new Error();
  }
  let ret = [];
  for (let i = 0; i < array1.length; i++) {
    ret.push(array1[i] + array2[i]);
  }
  return ret;
}