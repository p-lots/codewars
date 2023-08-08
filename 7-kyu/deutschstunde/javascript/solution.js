const derDieDas = wort => {
  const vowelsGer = "aeiouäöü";
  const isVowel = letter => vowelsGer.includes(letter.toLowerCase());
  const vowelCount = wort.split("").filter(isVowel).length;
  let article = "";
  if (vowelCount < 2) {
    article = "das";
  } else if (vowelCount < 4) {
    article = "die";
  } else {
    article = "der";
  }
  return `${article} ${wort}`;
};
