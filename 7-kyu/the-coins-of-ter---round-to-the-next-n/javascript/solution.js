const adjust = (coin, price) =>{
  let adjusted = price;
  while (adjusted % coin !== 0) {
    adjusted++;
  }
  return adjusted;
};
