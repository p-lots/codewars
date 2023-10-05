const getCharacters = (obj, key, val) => {
  const foundCharacters = [];
  const chars = obj.characters;
  for (let i = 0; i < chars.length; i++) {
    if (chars[i].hasOwnProperty(key) && chars[i][key].toLowerCase() === val.toLowerCase()) {
      foundCharacters.push(chars[i]);
    }
  }
  return foundCharacters;
};
