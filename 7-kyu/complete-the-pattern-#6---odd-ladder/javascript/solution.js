const pattern = n => {
  const staircase = [];
  for (let i = 1; i <= n; i += 2) {
    const line = Array(i).fill(i).join("");
    staircase.push(line);
  }
  return staircase.join("\n");
};
