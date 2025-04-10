const lottery = str => {
  const filtered = str.split("").filter(ch => /[0-9]/.test(ch));
  if (filtered.length === 0) {
    return "One more run!";
  }
  const digits = [...new Set(filtered)].join("");
  return digits;
};
