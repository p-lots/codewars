const vowelHelper = letter => !"aeiou".includes(letter.toLowerCase());

const smallWordHelper = sentence => {
  return sentence.split(" ")
    .map((word) => word.length < 4 ? word.toUpperCase() : word.split("").filter(vowelHelper).join(""))
    .join(" ");
};
