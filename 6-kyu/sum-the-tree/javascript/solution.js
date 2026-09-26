function sumTheTreeValues(root) {
  let sum = root.value ?? 0;
  for (const val of Object.values(root)) {
    if (val !== null) {
      sum += sumTheTreeValues(val);
    }
  }
  return sum;
}