const reverse = str => str.trim().split(" ").map((word, i) => i % 2 === 1 ? word.split("").reverse().join("") : word).join(" ");
