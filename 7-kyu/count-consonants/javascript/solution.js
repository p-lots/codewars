const consonantCount = str => {
  const vowels = "aeiou";
  const isAlpha = letter => /[a-z]/.test(letter);
  return str.toLowerCase()
    .split("")
    .filter(ch => isAlpha(ch) && !vowels.includes(ch))
    .length;
}