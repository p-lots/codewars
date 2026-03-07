const gracefulTipping = (bill) =>{
  let grandTotal = Math.ceil(bill * 1.15);
  console.log(grandTotal);
  if (grandTotal < 10) {
    return grandTotal;
  }
  const powerOfTen = Math.floor(Math.log10(grandTotal)) - 1;
  while (grandTotal % (5 * Math.pow(10, powerOfTen)) !== 0) {
    grandTotal++;
  }
  return grandTotal;
};
