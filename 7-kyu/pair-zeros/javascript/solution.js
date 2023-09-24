function pairZeros(arr) {
  let arry = arr;
  for (let i = 0; i < arry.length; i++) {
    if (arry[i] === 0) {
      for (let j = i + 1; j < arry.length; j++) {
        if (arry[j] === 0) {
          arry[j] = -1;
          break;
        }
      }
    }
  }
  const paired = arry.filter(elem => elem !== -1);
  return paired;
}