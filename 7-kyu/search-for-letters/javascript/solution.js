const change = strng => {
  const ret = "0".repeat(26).split("");
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  for (const ch of strng) {
    const idx = alphabet.indexOf(ch.toLowerCase());
    if (idx !== -1) {
      ret[idx] = "1";
    }
  }
  return ret.join("");
};
