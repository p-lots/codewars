const color2grey = (image) => {
  const newImage = [];
  for (const row of image) {
    const newRow = [];
    for (const pixel of row) {
      const average = Math.round(pixel.reduce((acc, nxt) => acc + nxt, 0) / pixel.length);
      const newPixel = [average, average, average];
      newRow.push(newPixel);
    }
    newImage.push(newRow);
  }
  return newImage;
};
