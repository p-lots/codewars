const squareOrSquareRoot = (array) => {
  const isPerfectSquare = (n) => Math.floor(n ** 0.5) * Math.floor(n ** 0.5) === n;
  return array.map((elem) => isPerfectSquare(elem) ? Math.floor(elem ** 0.5) : elem * elem);
};
