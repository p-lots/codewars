const decodePass = (passArr, bin) => {
  const binDecoded = bin.split(' ').map((elem) => String.fromCharCode(parseInt(elem, 2))).join('');
  return passArr.includes(binDecoded) ? binDecoded : false;
};
