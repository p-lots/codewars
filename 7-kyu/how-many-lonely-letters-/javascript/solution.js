const countLonelyLetters = text => {
  let lonelyCount = 0;
  for (let i = 0; i < text.length; i++) {
    if (/[^a-z]/i.test(text[i])) {
      continue;
    }
    const letter = text[i].toLowerCase();
    const prevLetter = String.fromCharCode(letter.charCodeAt(0) - 1);
    const nextLetter = String.fromCharCode(letter.charCodeAt(0) + 1);
    if (text.split("").filter(ch => ch.toLowerCase() === letter).length === 1 &&
        !text.toLowerCase().includes(prevLetter) && !text.toLowerCase().includes(nextLetter)) {
      
        lonelyCount++;
    }
  }
  return lonelyCount;
};
