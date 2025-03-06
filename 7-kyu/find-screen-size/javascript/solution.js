const findScreenHeight = (width, ratio) => {
  const [ ratioWidth, ratioHeight ] = ratio.split(":").map(Number);
  const resolution = `${width}x${Math.floor(width * ratioHeight / ratioWidth)}`;
  return resolution;
};
