const moveTen = s => {
  const mapFunc = ch => {
    let ret = ch.charCodeAt() + 10;
    if (ret > ('a'.charCodeAt() + 25)) {
      ret -= 26;
    }
    return String.fromCharCode(ret);
  };
  return s.split("").map(mapFunc).join("");
};
