const fistBeard = arr => {
  let ret = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      ret.push(arr[i][j]);
    }
  }
  return ret.map(elem => String.fromCharCode(elem)).join("");
}