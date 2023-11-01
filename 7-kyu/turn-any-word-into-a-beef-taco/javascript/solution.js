const tacofy = (word) => {
  const ingredients = {"a": "beef", "e": "beef", "i": "beef", "o": "beef", "u": "beef",
                       "t": "tomato", "l": "lettuce", "c": "cheese", "g": "guacamole", "s": "salsa"};
  let ret = ["shell"];
  const insides = word.split("").filter((elem) => ingredients.hasOwnProperty(elem.toLowerCase())).map((ch) => ingredients[ch.toLowerCase()]);
  ret = ret.concat(insides);
  ret.push("shell");
  return ret;
};
