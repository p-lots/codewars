const randomCase = x => x.split("").map(ch => Math.random() > 0.5 ? ch.toUpperCase() : ch.toLowerCase()).join("");
