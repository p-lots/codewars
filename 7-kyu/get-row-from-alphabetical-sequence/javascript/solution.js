const upperAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const getRow = n => {
  const adjN = n - 1;
  const rowNum = adjN % 26;
  const row = `${upperAlpha[rowNum].repeat(rowNum + 1)}${upperAlpha.slice(rowNum + 1)}`;
  return row;
};
