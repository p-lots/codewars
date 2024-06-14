const stringMerge = (string1, string2, letter) => {
  const str1Idx = string1.indexOf(letter);
  const str2Idx = string2.indexOf(letter);
  const merged = `${string1.slice(0, str1Idx)}${string2.slice(str2Idx)}`;
  return merged;
};
