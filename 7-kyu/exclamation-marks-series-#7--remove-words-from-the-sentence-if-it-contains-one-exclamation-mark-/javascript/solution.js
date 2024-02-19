const remove = string => {
  const count = (str, ch) => [...str].filter(elem => elem === ch).length;
  const noSingleExclamation = string.split(" ").filter(word => count(word, "!") !== 1).join(" ");
  return noSingleExclamation;
};
