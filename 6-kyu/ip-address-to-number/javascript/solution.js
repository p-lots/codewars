const ipToNum = ip => {
  const octets = ip.split(".").map(n => Number(n).toString(2).padStart(8, '0'));
  const joined = octets.join("");
  const baseTen = Number.parseInt(joined, 2);
  return baseTen;
};

const numToIp = num => {
  const baseTwo = num.toString(2).padStart(32, '0');
  const octets = [];
  for (let i = 0; i < baseTwo.length; i += 8) {
    const octet = baseTwo.slice(i, i + 8);
    octets.push(octet);
  }
  return octets.map(n => Number.parseInt(n, 2)).join(".");
};