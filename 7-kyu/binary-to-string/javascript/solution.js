const binaryToString = binary => binary.split("0b").filter(Boolean).map(n => String.fromCharCode(Number.parseInt(n, 2))).join("");
