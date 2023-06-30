const findNb = m => {
  let ret = 0;
  while (true) {
    ret++;
    m -= ret ** 3;
    if (m === 0) {
      return ret;
    } else if (m < 0) {
      return -1;
    }
  }
};

