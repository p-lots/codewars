const alphaSeq = str => str.toLowerCase().split("").sort().map(ch => ch.toUpperCase() + ch.repeat(ch.charCodeAt(0) - 97)).join(",");
