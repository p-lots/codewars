const isValidIP = str => {
  const octets = str.split(".");
  if (octets.length !== 4) {
    return false;
  }
  if (!octets.every(oct => /^\d{1,3}$/g.test(oct)) || octets.some(oct => oct.length !== 1 && oct[0] === "0")) {
    return false;
  }
  const octetsNum = octets.map(Number);
  if (octetsNum.some(n => n < 0 || n > 255)) {
    return false;
  }
  return true;
};