const reOrdering = (text) => {
  const textSplit = text.split(" ");
  if (textSplit.length === 1) {
    return textSplit.join(" ");
  }
  for (let i = 0; i < textSplit.length; i++) {
    if (textSplit[i][0].toUpperCase() === textSplit[i][0]) {
      for (let j = i; j >= 1; j--) {
        const temp = textSplit[j - 1];
        textSplit[j - 1] = textSplit[j];
        textSplit[j] = temp;
      }
      break;
    }
  }
  const result = textSplit.join(" ");
  return result;
};
