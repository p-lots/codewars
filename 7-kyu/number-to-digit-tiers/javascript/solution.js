function createArrayOfTiers(num) {
  const numStr = num.toString();
  return Array.from({ length: numStr.length }, (_, idx) => numStr.slice(0, idx + 1));
}