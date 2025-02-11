const deEmojify = emojiString => {
  const words = emojiString.split("  ");
  const emojiLookup = {
    ":)": "0", ":D": "1", ">(": "2", ">:C": "3", 
    ":/": "4", ":|": "5", ":O": "6", ";)": "7", 
    "^.^": "8", ":(": "9"
  };
  return words.map(word => {
    const splitWord = word.split(" ");
    const translatedWord = splitWord.map(emoji => emojiLookup[emoji]);
    const letter = String.fromCharCode(Number(translatedWord.join("")));
    return letter;
  }).join("");
};
