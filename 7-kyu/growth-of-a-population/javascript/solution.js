const nbYear = (p0, percent, aug, p) => {
  percent /= 100.0;
  let years = 0;
  while (p0 < p) {
    p0 += p0 * percent + aug;
    years++;
  }
  return years;
}