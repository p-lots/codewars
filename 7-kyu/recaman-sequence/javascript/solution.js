function recaman(n) {
  const banned = new Set();
  let member = 0;
  for (let i = 0; i <= n; i++) {
    const diff = member - i;
    member = (diff < 0 || banned.has(diff)) ? member + i : diff;
    banned.add(member);
  }
  return member;
}