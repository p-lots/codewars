const dotCalculator = (equation) => {
	const eqSplit = equation.split(" ");
  const lhs = eqSplit[0].length;
  const oper = eqSplit[1];
  const rhs = eqSplit[2].length;
  let result = 0;
  if (oper === "+") {
    result = lhs + rhs;
  } else if (oper === "-") {
    result = lhs - rhs;
  } else if (oper === "*") {
    result = lhs * rhs;
  } else if (oper === "//") {
    result = Math.floor(lhs / rhs);
  }
  return ".".repeat(result);
}