int getPerimeter(int length, int width) {
  // standard formula: l * 2 + w * 2
  // factor out the 2: 2 * (l + w)
  return 2 * (length + width);
}