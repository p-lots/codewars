const rgb = (r, g, b) => {
  const clamp = (n) => Math.min(Math.max(n, 0), 255);
  const toHex = (n) => {
    let result = clamp(n).toString(16).toUpperCase();
    if (result.length < 2) {
      result = "0" + result;
    }
    return result;
  }
  return `${toHex(r)}${toHex(g)}${toHex(b)}`;
};
