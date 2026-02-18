function allNonConsecutive(arr) {
  const nonConsecutive = [];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] !== arr[i - 1] + 1) {
      const next = { i: i, n: arr[i] };
      nonConsecutive.push(next);
    }
  }
  return nonConsecutive;
}
