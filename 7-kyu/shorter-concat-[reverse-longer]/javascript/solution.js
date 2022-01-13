const shorter_reverse_longer = (a, b) => {
  let short = a.length < b.length ? a : b;
  let long = a.length > b.length ? a : b;
  if (a.length === b.length) {
    short = b;
    long = a;
  }
  return `${short}${long.split('').reverse().join('')}${short}`
}