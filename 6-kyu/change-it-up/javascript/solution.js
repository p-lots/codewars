const changer = str => {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  return [...str].map(char => {
    if (/[^a-z]/i.test(char)) {
      return char;
    }
    const nextIdx = (alphabet.indexOf(char.toLowerCase()) + 1) % alphabet.length;
    let nextCh = alphabet[nextIdx];
    if (/[aeiou]/i.test(nextCh)) {
      nextCh = nextCh.toUpperCase();
    }
    return nextCh;
  }).join("");
};
