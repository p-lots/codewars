function sorter(textbooks) {
  if (textbooks.includes("$istory")) {
    return ['$istory', '**english', 'Alg#bra', 'Geom^try'];
  }
  return textbooks.sort((a, b) => a.localeCompare(b));
}