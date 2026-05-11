function diff(s1, s2){
  return new Set([...s1].filter(elem => !s2.has(elem)));
}