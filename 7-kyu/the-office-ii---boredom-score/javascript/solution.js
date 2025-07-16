const boredom = staff => {
  const boredomLookup = {
    "accounts": 1, "finance": 2, "canteen": 10, "regulation": 3,
    "trading": 6, "change": 6, "IS": 8, "retail": 5, "cleaning": 4,
    "pissing about": 25
  };
  const boredomValue = Object.values(staff)
    .map(dept => boredomLookup[dept] || 0)
    .reduce((acc, nxt) => acc + nxt, 0);
  if (boredomValue <= 80) {
    return "kill me now";
  } else if (boredomValue > 80 && boredomValue < 100) {
    return "i can handle this";
  }
  return "party time!!";
};
