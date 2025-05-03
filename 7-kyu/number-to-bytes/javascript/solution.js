const toBytes = n => {
	let nBin = n.toString(2);
  while (nBin.length % 8 !== 0) {
    nBin = "0" + nBin;
  }
  const bytes = [];
  for (let i = 0; i < nBin.length; i += 8) {
    const byte = nBin.slice(i, i + 8);
    bytes.push(byte);
  }
  return bytes;
};
