const testResult = array => {
  const average = Math.round((array.reduce((acc, nxt) => acc + nxt, 0) / array.length) * 1000) / 1000;
  const dict = {h: 0, a: 0, l: 0};
  for (const mark of array) {
    if (mark < 7) {
      dict.l++;
    } else if (mark < 9) {
      dict.a++;
    } else {
      dict.h++;
    }
  }
  const result = [average, dict];
  if (array.every(mark => mark > 8)) {
    result.push("They did well");
  }
  return result;
};
