export const countSheep = (num: number): string => {
  const murmur = [];
  for (let i = 1; i <= num; i++) {
    const mumbling = `${i} sheep...`;
    murmur.push(mumbling);
  }
  return murmur.join("");
};
