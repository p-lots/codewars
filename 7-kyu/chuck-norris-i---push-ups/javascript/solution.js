const chuckPushUps = st => {
  if (typeof st !== "string" || st.length === 0) {
    return "FAIL!!";
  }
  const numbers = st.split(" ")
    .map(elem => elem.split("").filter(ch => ch === "1" || ch === "0").join(""))
    .filter(elem => elem.length > 1);
  if (numbers.length === 0) {
    return "CHUCK SMASH!!";
  }
  return Math.max(...(numbers.map(n => parseInt(n, 2))));
};
