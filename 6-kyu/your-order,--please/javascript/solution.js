const extractNumber = word => Number(word.match(/\d/));

const order = words => words.split(" ").sort((a, b) => extractNumber(a) - extractNumber(b)).join(" ");
