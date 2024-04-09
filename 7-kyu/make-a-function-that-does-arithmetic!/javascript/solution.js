const arithmetic = (a, b, operator) => {
  const lookup = {add: (x, y) => x + y, subtract: (x, y) => x - y,
                  multiply: (x, y) => x * y, divide: (x, y) => x / y};
  return lookup[operator](a, b);
};
