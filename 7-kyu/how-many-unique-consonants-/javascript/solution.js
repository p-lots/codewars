const countConsonants = str => {
  const regex = /[bcdfghjklmnpqrstvwxyz]/i;
  const consonantsOnly = str.toLowerCase()
    .split("")
    .filter(ch => regex.test(ch));
  return (new Set(consonantsOnly)).size;
};
