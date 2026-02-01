const getIssuer = number => {
  const numStr = number.toString();
  if (numStr.length === 15 && (numStr.slice(0, 2) === "34" || numStr.slice(0, 2) === "37")) {
    return "AMEX";
  } else if (numStr.length === 16 && numStr.slice(0, 4) === "6011") {
    return "Discover";
  } else if (numStr.length === 16 && Number(numStr.slice(0, 2)) >= 51 && Number(numStr.slice(0, 2)) <= 55) {
    return "Mastercard";
  } else if ((numStr.length === 13 || numStr.length === 16) && numStr[0] === "4") {
    return "VISA";
  }
  return "Unknown";
};
