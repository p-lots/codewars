function areEqual(s1, s2){
  return s1.size === s2.size && [...s1].every(elem => s2.has(elem));
}

function notEqual(s1, s2){
  return [...s1].some(elem => !s2.has(elem)) || [...s2].some(elem => !s1.has(elem));
}
