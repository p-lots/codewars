const xMarksTheSpot = input => {
  let xCoords = [];
  let xCount = 0;
  for (let i = 0; i < input.length; i++) {
    for (let j = 0; j < input[i].length; j++) {
      if (input[i][j] === "x") {
        xCoords = [i, j];
        xCount++;
      }
    }
  }
  return xCount === 1 ? xCoords : [];
};
