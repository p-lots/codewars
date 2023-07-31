const sortLetters = letters => {
  let ret = [[], []];
  for (const row of letters) {
    for (const letter of row) {
      if (typeof letter === "string") {
        if ("aeiou".includes(letter.toLowerCase())) {
          ret[0].push(letter.toUpperCase());
        } else {
          ret[1].push(letter.toUpperCase());
        }
      }
    }
  }
  return ret;
};
