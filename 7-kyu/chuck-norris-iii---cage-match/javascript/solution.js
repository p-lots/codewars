const headSmash = arr => {
  if (typeof arr === "number") {
    return "This isn't the gym!!";
  }
  return arr.length > 0 ? arr.map(line => line.includes("O") ? line.replace(/O/g, " ") : line) : "Gym is empty";
};
