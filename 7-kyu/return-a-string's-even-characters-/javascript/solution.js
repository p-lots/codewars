const evenChars = (string) => string.length > 1 && string.length < 101 ? string.split("").filter((ch, idx) => idx % 2 === 1) : "invalid string";
