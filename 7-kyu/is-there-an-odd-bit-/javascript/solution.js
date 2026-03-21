const anyOdd = x => {
  const bin = x.toString(2).split("").reverse().join("");
  for (let i = 0; i < bin.length; i++) {
    if (i % 2 === 1 && bin[i] === "1") {
      return 1;
    }
  }
  return 0;
};
