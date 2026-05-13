function isSubsetOf(s1, s2) {
  return [...s1].every(elem => s2.has(elem));
}

function isSupersetOf(s1, s2) {
  return isSubsetOf(s2, s1);
}