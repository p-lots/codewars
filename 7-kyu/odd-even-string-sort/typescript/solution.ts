export const sortMyString = (str: string): string => {
  const evenIdxs: string = str.split("")
    .filter((ch, idx) => idx % 2 === 0)
    .join("");
  const oddIdxs: string = str.split("")
    .filter((ch, idx) => idx % 2 === 1)
    .join("");
  const joined: string = `${evenIdxs} ${oddIdxs}`;
  return joined;
};
