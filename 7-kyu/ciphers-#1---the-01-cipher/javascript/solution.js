const encode = plaintext => {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  return plaintext.split("").map(ch => /[^a-z]/i.test(ch) ? ch : (alphabet.indexOf(ch.toLowerCase()) % 2 === 0 ? "0" : "1")).join("")
};
