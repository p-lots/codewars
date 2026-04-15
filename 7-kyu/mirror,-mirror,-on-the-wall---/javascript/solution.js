const mirror = data => {
  if (data.length < 2) {
    return data;
  }
  let dta = [...data];
  dta = dta.sort((a, b) => a - b);
  return [...dta, ...(dta.slice(0, dta.length - 1).reverse())];
};
