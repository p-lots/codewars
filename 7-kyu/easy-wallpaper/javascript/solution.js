const wallpaper = (l, w, h) => {
  const number_words = ["zero", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty"];
  if (!(l > 0 && w > 0 && h > 0)) return number_words[0];
  const index = Math.ceil(((2.0 * w * h) + (2.0 * h * l)) * 1.15 / 5.2)
  return number_words[index]
}