const loopArr = (arr, direction, steps) => {
  let ret = [];
  if (direction === "right") {
    ret = arr.slice(-steps);
  } else {
    ret = arr.slice(steps);
  }
  for (let i = 0; ret.length < arr.length; i++) {
    ret.push(arr[i % arr.length]);
  }
  return ret;
}