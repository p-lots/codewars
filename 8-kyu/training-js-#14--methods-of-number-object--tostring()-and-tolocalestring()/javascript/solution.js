const colorToHex = (color) => color.toString(16).padStart(2, "0");

const colorOf = (r, g, b) => `#${colorToHex(r)}${colorToHex(g)}${colorToHex(b)}`;
