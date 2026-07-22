const vowel2index = (str) => str.split("").map((ch, idx) => /[aeiou]/gi.test(ch) ? `${idx + 1}` : ch).join("");
