const wordsToMarks = string => string.split("").reduce((acc, nxt) => acc + (nxt.charCodeAt(0) - 'a'.charCodeAt(0) + 1), 0);
