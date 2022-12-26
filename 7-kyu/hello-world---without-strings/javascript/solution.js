const helloWorld = () => {
  const magicNumbers = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33];
  let ret = new String();
  for (const n of magicNumbers) {
    ret += String.fromCharCode(n);
  }
  return ret;
};
