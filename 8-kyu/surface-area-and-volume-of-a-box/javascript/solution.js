const getSize = (width, height, depth) => {
  const surfaceArea = width * height * 2 + height * depth * 2 + depth * width * 2;
  const volume = width * height * depth;
  return [surfaceArea, volume];
};

