const evenator = str => str.replace(/[\.,\?\!_]/g, "")
  .split(" ")
  .map(word => word.length % 2 === 0 ? word : word + word.slice(-1))
  .join(" ");
