const histogram = results => {
  return results.reverse().map((result, idx) => {
    const line = `${results.length - idx}|${result > 0 ? "#".repeat(result) + " " + result.toString() : ""}\n`;
    return line;
  }).join("");
};
