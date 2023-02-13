const sortVowels = s => {
  if (typeof s !== 'string') {
    return '';
  }
  let ret = [];
  const vowels = 'aeiou';
  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i].toLowerCase())) {
      ret.push(`|${s[i]}`);
    } else {
      ret.push(`${s[i]}|`);
    }
  }
  return ret.join('\n');
};