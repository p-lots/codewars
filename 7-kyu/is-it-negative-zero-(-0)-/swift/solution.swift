func isNegativeZero(_ n: Float) -> Bool {
  let negZero: Float = -0.0
  return negZero == n && negZero.sign == n.sign
}