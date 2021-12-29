const solution = digits => {
  let greatest = parseInt(digits.slice(0, 5));
  for (let i = 0; i < digits.length - 4; i++) {
    if (parseInt(digits.slice(i, i + 5)) > greatest) {
      greatest = parseInt(digits.slice(i, i + 5));
    }
  }
  return greatest;
};