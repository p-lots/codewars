const nameThatNumber = num => {
  const ones = ["zero", "one", "two", "three", "four", "five", "six", "seven",
                "eight", "nine"];
  const teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                 "sixteen", "seventeen", "eighteen", "nineteen"];
  const tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
                "seventy", "eighty", "ninety"];
  if (num < 10) {
    return ones[num];
  } else if (num >= 10 && num < 20) {
    return teens[num % 10];
  }
  const tensPlace = Math.floor(num / 10);
  const onesPlace = num % 10;
  return onesPlace > 0 ? `${tens[tensPlace]} ${ones[onesPlace]}` : `${tens[tensPlace]}`;
};
