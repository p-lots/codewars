const duplicates = (arr) => {
  const foundDupes = [];
  const seenElems = [];
  for (const elem of arr) {
    if (!seenElems.includes(elem)) {
      seenElems.push(elem);
    } else if (!foundDupes.includes(elem)) {
      foundDupes.push(elem);
    }
  }
  return foundDupes;
};
