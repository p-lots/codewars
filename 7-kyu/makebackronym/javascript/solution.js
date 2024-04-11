// preload variable: dict

const makeBackronym = string => string.split("")
  .map(letter => dict[letter.toUpperCase()])
  .join(" ");
