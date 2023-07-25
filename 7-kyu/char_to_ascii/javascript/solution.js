const charToAscii = str => {
  const strAlpha = str.replace(/\W/g, "");
  if (strAlpha.length === 0) {
    return null;
  }
  const setFromStr = new Set(strAlpha);
  const hash = {};
  setFromStr.forEach((ch) => {
    hash[ch] = ch.charCodeAt();
  });
  return hash;
};
