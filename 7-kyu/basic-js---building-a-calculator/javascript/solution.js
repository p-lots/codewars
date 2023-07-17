class Calculator {
  static add(lhs, rhs) {
    return lhs + rhs;
  }
  
  static subtract(lhs, rhs) {
    return lhs - rhs;
  }
  
  static multiply(lhs, rhs) {
    return lhs * rhs;
  }
  
  static divide(lhs, rhs) {
    return rhs !== 0 ? lhs / rhs : false;
  }
}