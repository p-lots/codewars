const solve = arr => {  
  let ret = [];
  for (const word of arr) {
    let charsMatching = 0;
    for (let i = 0; i < word.length; i++) {
      const wordLower = word.toLowerCase();
      if (wordLower.charCodeAt(i) - 97 == i) charsMatching++; // charCode of 'a' == 97
    }
    ret.push(charsMatching);
  }
  return ret;
};
