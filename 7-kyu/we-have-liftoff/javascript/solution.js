const liftoff = (instructions) => {
  let sorted = instructions.sort((a, b) => b - a).map((elem) => elem.toString()).join(' ');
  return sorted + " liftoff!";
};