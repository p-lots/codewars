const christmasTree = height => {
  let ret = [];
  for (let i = 0; i < height; i++) {
    const spaces = " ".repeat(height - i - 1);
    const stars = "*".repeat(i * 2 + 1);
    ret.push(spaces + stars + spaces);
  }
  return ret.join("\n");
}