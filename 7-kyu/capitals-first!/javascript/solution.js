const capitalsFirst = str => {
  const onlyValid = str.split(" ").filter(word => /[a-z]/i.test(word[0]));
  const capitals = onlyValid.filter(word => word[0] === word[0].toUpperCase());
  const lowerCase = onlyValid.filter(word => word[0] === word[0].toLowerCase());
  return capitals.concat(lowerCase).join(" ");
};
