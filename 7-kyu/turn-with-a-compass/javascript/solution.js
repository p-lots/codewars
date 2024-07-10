const changeDirection = (dirs, facing, turn) => {
  const currentDir = dirs.indexOf(facing) + Math.floor(turn / 45);
  return dirs[currentDir % dirs.length];
};

const direction = (facing, turn) => {
  const clockwise = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"];
  const counterClockwise = ["N", "NW", "W", "SW", "S", "SE", "E", "NE"];
  return turn > 0 ? changeDirection(clockwise, facing, turn) : changeDirection(counterClockwise, facing, Math.abs(turn));
};
