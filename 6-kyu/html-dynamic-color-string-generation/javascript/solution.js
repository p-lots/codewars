const generateColor = () => {
  const generateRandomHex = () => {
    return Math.floor(255 * Math.random()).toString(16);
  };
  return `#${generateRandomHex()}${generateRandomHex()}${generateRandomHex()}`;
};