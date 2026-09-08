const nextId = (ids) => {
  const uniqueIds = [...(new Set(ids))].sort((a, b) => a - b);
  for (let i = 0, j = 0; i < uniqueIds.length; i++, j++) {
    if (uniqueIds[i] !== j) {
      return j;
    }
  }
  return uniqueIds.length;
}