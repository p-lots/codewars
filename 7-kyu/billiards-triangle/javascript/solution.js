const pyramid = balls => {
  let ret = 0;
  let nextRow = 1;
  while (balls > 0) {
    ret++;
    nextRow++;
    balls -= nextRow;
  }
  return ret;
}