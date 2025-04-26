const naughtyOrNice = data => {
  let count = 0;
  for (const [month, monthData] of Object.entries(data)) {
    for (const [day, result] of Object.entries(monthData)) {
      count += result === "Nice" ? 1 : -1;
    }
  }
  return count < 0 ? "Naughty!" : "Nice!";
};
