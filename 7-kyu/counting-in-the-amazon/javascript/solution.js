const countArara = (n) => n === 1 ? "anane" : Array(Math.floor(n / 2)).fill("adak").join(" ") + (n % 2 !== 0 ? " anane" : "");
