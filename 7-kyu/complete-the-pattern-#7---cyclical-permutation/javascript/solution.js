const pattern = n => {
  const rows = [];
  for (let i = 1; i <= n; i++) {
    const row = [];
    for (let j = i; j < n + i; j++) {
      const nextChar = `${j > n ? j % n : j}`;
      row.push(nextChar);
    }
    const joined = row.join("");
    rows.push(joined);
  }
  return rows.join("\n");
};
