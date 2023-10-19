const comparator = (a, b) => {
  const aSplit = a.split(" ");
  const bSplit = b.split(" ");
  if (/^[a-zA-Z]/.test(aSplit[0])) {
    if (/^[a-zA-Z]/.test(bSplit[0])) {
      return bSplit[0][0] - aSplit[0][0];
    }
    if (aSplit[0][0] === "a") {
      return 1;
    }
    if (aSplit[0][0] === "O") {
      return -1;
    }
  } else if (/^[a-zA-Z]/.test(bSplit[0])) {
    if (bSplit[0][0] === "a") {
      return -1;
    }
    if (bSplit[0][0] === "O") {
      return 1;
    }
  }
  return bSplit[0] - aSplit[0];
}