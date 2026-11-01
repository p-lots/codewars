const fridgeOrganizer = items => {
  return items.filter(item => item.expiryDays >= 0).sort((a, b) => {
    if (a.isAlmostEmpty && !b.isAlmostEmpty) {
      return -1;
    } else if (!a.isAlmostEmpty && b.isAlmostEmpty) {
      return 1;
    }
    if (a.expiryDays === b.expiryDays) {
      return a.name.localeCompare(b.name);
    }
    return a.expiryDays - b.expiryDays;
  }).map(item => item.name);
};
