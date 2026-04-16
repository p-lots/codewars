const mirror = (code, key = "abcdefghijklmnopqrstuvwxyz") => {
  const lookup = {};
  for (let i = 0; i < key.length; i++) {
    lookup[key[i]] = key[key.length - i - 1];
  }
  return code.toLowerCase().split("").map(ch => lookup[ch] || ch).join("");
};
