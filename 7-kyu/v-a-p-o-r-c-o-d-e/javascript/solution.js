const vaporcode = string => string.replace(/ /g, "").split("").map((elem) => elem.toUpperCase()).join("  ");
