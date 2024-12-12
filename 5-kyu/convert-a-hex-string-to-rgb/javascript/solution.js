const hexStringToRGB = hexString => {
  hexString = hexString.slice(1).toUpperCase();
  return { r: parseInt(hexString.slice(0, 2), 16),
          g: parseInt(hexString.slice(2, 4), 16),
          b: parseInt(hexString.slice(4), 16) };
}