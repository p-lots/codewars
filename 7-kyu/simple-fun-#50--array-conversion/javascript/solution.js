const arrayConversion = (arr) => {
  let array = arr.map(elem => elem);
  let iter = 0;
  while (array.length > 1) {
    let temp = [];
    if (iter % 2 === 0) {
      for (let i = 0; i < array.length - 1; i += 2) {
        temp.push(array[i] + array[i + 1]);
      }
      array = temp;
    } else {
      for (let i = 0; i < array.length- 1; i += 2) {
        temp.push(array[i] * array[i + 1])
      }
      array = temp;
    }
    iter++;
  }
  return array[0];
};
