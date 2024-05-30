const reverseLetter = str => str.split("")
    .filter(char => /[a-z]/ig.test(char))
    .reverse()
    .join("");
