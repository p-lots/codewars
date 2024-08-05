// return price without vat
const excludingVatPrice = price => {
  return !price && price !== 0 ? -1 : Math.round((price / 1.15) * 100) / 100;
};
