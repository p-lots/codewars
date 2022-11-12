const isSameLanguage = (list) => {
  for (const obj of list) {
    if (obj.language !== list[0].language) {
      return false;
    }
  }
  return true;
};
