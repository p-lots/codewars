const rgbToGrayscale = color => { 
  const red = Number.parseInt(color.slice(1, 3), 16);
  const green = Number.parseInt(color.slice(3, 5), 16);
  const blue = Number.parseInt(color.slice(5), 16);
  const lum = Math.round(0.299 * red + 0.587 * green + 0.114 * blue);
  return `#${lum.toString(16).padStart(2, "0").repeat(3)}`;
}