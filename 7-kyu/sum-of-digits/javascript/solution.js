const sum = digits => {
  if (typeof digits === "undefined") {
    return "";
  }
  else if (typeof digits === "number") {
    digits = digits.toString();
  }
  const total = digits.split("").reduce((acc, nxt) => acc + parseInt(nxt), 0);
  return `${digits.split("").join(" + ")} = ${total}`;
};
