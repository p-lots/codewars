const encode = str => {
  const translation = {
    a: "g", g: "a", d: "e", e: "d",
    r: "y", y: "r", p: "o", o: "p",
    l: "u", u: "l", k: "i", i: "k"
  };
  return str.split("")
    .map(ch => {
      const translated = translation[ch.toLowerCase()] || ch;
      return ch.toLowerCase() === ch ? translated : translated.toUpperCase();
    })
    .join("");
};


const decode = str => {
  return encode(str);
};
