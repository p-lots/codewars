const uncensor = (infected, discovered) => {
  let ret = "";
  discovered = discovered.split("");
  for (const ch of infected) {
    if (ch === "*") {
      const next = discovered.shift();
      ret += next;
    } else {
      ret += ch;
    }
  }
  return ret;
};
