const reverseAndMirror = (s1, s2) => {
  const firstHalf = s2.split("")
    .reverse()
    .map(ch => ch === ch.toUpperCase() ? ch.toLowerCase() : ch.toUpperCase())
    .join("");
  const secondHalf = s1.split("")
    .map(ch => ch === ch.toUpperCase() ? ch.toLowerCase() : ch.toUpperCase())
    .join("");
  return `${firstHalf}@@@${secondHalf.split("").reverse().join("")}${secondHalf}`;
};
