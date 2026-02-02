const convertBits = (a, b) => (a ^ b).toString(2).split("").filter(ch => ch === "1").length;
