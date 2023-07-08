function isIsogram(str){
  let seenLetters = [];
  for (const ch of str.toLowerCase()) {
    if (!seenLetters.includes(ch)) {
      seenLetters.push(ch);
    } else {
      return false;
    }
  }
  return true;
}