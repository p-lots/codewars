export const basicOp = (operation: string, value1: number, value2: number): number => {
  switch (operation) {
      case "+":
      return value1 + value2;
      case "-":
      return value1 - value2;
      case "*":
      return value1 * value2;
      case "/":
      return value1 / value2;
      default:
      return Number.MIN_SAFE_INTEGER;
  }
}