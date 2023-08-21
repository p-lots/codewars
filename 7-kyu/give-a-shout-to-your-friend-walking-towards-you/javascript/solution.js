const madShout = sidewalk => {
  const youIndex = sidewalk.indexOf("Y");
  const friendIndex = sidewalk.indexOf("F");
  const iCount = Math.max(1, Math.ceil((friendIndex - youIndex) / 2));
  const shout = `O${"i".repeat(iCount)} F!`;
  return shout;
};
