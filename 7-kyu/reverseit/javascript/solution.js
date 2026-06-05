const reverseIt = data => {
  if (!(typeof data === "number" || typeof data === "string")) {
    return data;
  }
  return typeof data === "string" ? data.split("").reverse().join("") : Number(`${data}`.split("").reverse().join(""));
};