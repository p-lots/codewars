const findSpaceship = map => {
  if (map) {
    const mapSplit = map.split("\n");
    for (let i = 0; i < mapSplit.length; i++) {
      const xCoord = mapSplit[i].split("").findIndex(val => val === "X");
      if (xCoord !== -1) {
        const yCoord = mapSplit.length - i - 1;
        return [xCoord, yCoord];
      }
    }
  }
  return "Spaceship lost forever.";
};
