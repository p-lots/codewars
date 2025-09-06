function countWords(str) {
  if (str.length === 0) {
    return 0;
  }
  const chars = ["-", "'", "`"];
  for (const char of chars) {
    str = str.replace(char, "");
  }
  return str.trim().split(/\w+/ig).length - 1;
}