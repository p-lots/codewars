const encode = (str) => {
  let ret = [];
  let currCh = str[0];
  let currCount = 1;
  for (let i = 1; i < str.length; i++) {
    if (currCh === str[i]) {
      currCount += 1;
    } else {
      ret.push([currCount, currCh]);
      currCount = 1;
      currCh = str[i];
    }
  }
  ret.push([currCount, currCh])
  return "[" + ret.map((elem) => `[${elem[0]},"${elem[1]}"]`).join(",") + "]";
};

const compress = (str) => {
  const encoded = encode(str);
  return encoded.length > str.length ? str : encoded;
};

const decode = (encoded) => {
  const arr = eval(encoded);
  let ret = "";
  for (const pair of arr) {
    const count = pair[0];
    const ch = pair[1];
    ret += ch.repeat(count);
  }
  return ret;
};

const decompress = (compressed) => {
  return compressed.includes("[") ? decode(compressed) : compressed;
};
