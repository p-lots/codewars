const solution = (fullText, searchText) => {
  let count = 0;
  let pos = fullText.indexOf(searchText);
  while (pos !== -1) {
    pos = fullText.indexOf(searchText, pos + 1);
    count++;
  }
  return count;
};
