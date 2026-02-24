const findMiddle = str => {
  if (typeof str !== 'string' || str.replace(/[^0-9]/g, "").length === 0) {
    return -1;
  }
  const product = str.split("").filter(chr => /[0-9]/.test(chr)).reduce((acc, nxt) => acc * nxt, 1).toString();
  const midIdx = Math.floor(product.length / 2);
  return product.length % 2 === 0 ? Number(product.slice(midIdx - 1, midIdx + 1)) : Number(product[midIdx]);
};
