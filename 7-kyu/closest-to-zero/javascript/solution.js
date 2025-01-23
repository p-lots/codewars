const closest = (arr) => {
  let smallestPos = Number.MAX_SAFE_INTEGER;
  let smallestNeg = Number.MAX_SAFE_INTEGER;
  let zeroFound = false;
  for (const num of arr) {
    if (num > 0) {
      smallestPos = Math.min(smallestPos, num);
    } else if (num < 0) {
      smallestNeg = Math.abs(num) < Math.abs(smallestNeg) ? num : smallestNeg;
    } else {
      zeroFound = true;
    }
  }
  let closestDiff;
  if (zeroFound) {
    closestDiff = 0;
  } else if (Math.abs(smallestPos) < Math.abs(smallestNeg)) {
    closestDiff = smallestPos;
  } else if (Math.abs(smallestPos) > Math.abs(smallestNeg)) {
    closestDiff = smallestNeg;
  } else {
    closestDiff = null;
  }
  return closestDiff;
}
