const getRectangleString = (width, height) => {
  const topLine = `${"*".repeat(width)}\r\n`;
  const midLine = width === 1 ? "" : `*${" ".repeat(width - 2)}*\r\n`;
  return height === 1 ? `${topLine}` : `${topLine}${midLine.repeat(height - 2)}${topLine}`;
}