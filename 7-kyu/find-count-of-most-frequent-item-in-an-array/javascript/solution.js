const mostFrequentItemCount = (collection) => {
  const countItems = (items) => {
    const itemCounts = {};
    for (const item of items) {
      if (!itemCounts.hasOwnProperty(item)) {
        itemCounts[item] = 1;
      } else {
        itemCounts[item]++;
      }
    }
    return itemCounts;
  };
  const counts = countItems(collection);
  let mostFrequentCount = 0;
  for (const item in counts) {
    mostFrequentCount = Math.max(mostFrequentCount, counts[item]);
  }
  return mostFrequentCount;
};
