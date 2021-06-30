const translate = word => {
  if (word.length < 2) {
    return word;
  }
  const firstLetter = word[0].toLowerCase();
  if (firstLetter === 'a' || firstLetter === 'e' || firstLetter === 'i' || firstLetter === 'o' || firstLetter === 'u') {
    return `${word}ay`;
  }
  return `${word.slice(1, word.length)}${word[0]}ay`
}