const alphabetWar = fight => {
  const leftLetters = {w: 4, p: 3, b: 2, s: 1};
  const rightLetters = {m: 4, q: 3, d: 2, z: 1};
  let leftSum = 0;
  let rightSum = 0;
  for (const ch of fight) {
    if (leftLetters[ch]) {
      leftSum += leftLetters[ch];
    } else if (rightLetters[ch]) {
      rightSum += rightLetters[ch];
    }
  }
  return leftSum > rightSum ? "Left side wins!" : leftSum === rightSum ? "Let's fight again!" : "Right side wins!";
};