function negationValue(string, value) {
  if (!string) {
    return !!value;
  }
  return string.length % 2 == 1 ? !value : !!value;
}