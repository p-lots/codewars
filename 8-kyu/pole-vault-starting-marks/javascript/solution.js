const startingMark = bodyHeight => {
  // Remember: Body height of 1.52 m --> starting mark: 9.45 m
  //           Body height of 1.83 m --> starting mark: 10.67 m
  // All other starting marks are based on these guidelines!
  return Math.round((bodyHeight * 3.935483871 + 3.468064516) * 100) / 100;
};
