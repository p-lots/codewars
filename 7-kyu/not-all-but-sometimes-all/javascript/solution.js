const remove = (str, what) => {
  let ret = JSON.parse(JSON.stringify(str));
  for (const [ch, count] of Object.entries(what)) {
    if (ret.includes(ch)) {
      let cnt = count;
      while (cnt--) {
        ret = ret.replace(ch, "");
      }
    }
  }
  return ret;
};
