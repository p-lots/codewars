const bulbMaze = (maze) => {
  if ([...maze].every((elem) => elem === maze[0]) && maze[0] !== " " || 
      [...maze].some((elem, i, arr) => elem !== " " && elem === arr[i + 1]) || 
      [...maze].some((elem, i) => elem === "o" && i % 2 === 0)) {
    return false;
  }
  return true;
};
