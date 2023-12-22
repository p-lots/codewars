function hasUniqueChars(str){
  const strSet = new Set(str);
  return strSet.size === str.length;
}