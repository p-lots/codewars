const updateLight = current => {
  const nextLight = {green: "yellow", yellow: "red", red: "green"};
  return nextLight[current];
}