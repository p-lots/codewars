const encode = str => {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  return str.split("").map(ch => alphabet.includes(ch.toLowerCase()) ? alphabet.indexOf(ch.toLowerCase()) + 1 : ch).join("");
};
