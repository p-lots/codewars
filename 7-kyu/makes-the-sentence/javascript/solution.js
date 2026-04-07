const makesTheSentence = (characterArray, sentenceString) => {
  const sentenceCharCounts = {};
  const arrCharCounts = {};
  for (const ch of sentenceString) {
    if (/\s/.test(ch)) {
      continue;
    }
    if (!Object.keys(sentenceCharCounts).includes(ch)) {
      sentenceCharCounts[ch] = 1;
    } else {
      sentenceCharCounts[ch] = sentenceCharCounts[ch] + 1;
    }
  }
  for (const ch of characterArray) {
    if (!Object.keys(arrCharCounts).includes(ch)) {
      arrCharCounts[ch] = 1;
    } else {
      arrCharCounts[ch] = arrCharCounts[ch] + 1;
    }
  }
  for (const [ch, count] of Object.entries(sentenceCharCounts)) {
    if (!Object.keys(arrCharCounts).includes(ch) || arrCharCounts[ch] !== count) {
      return false;
    }
  }
  return true;
};
