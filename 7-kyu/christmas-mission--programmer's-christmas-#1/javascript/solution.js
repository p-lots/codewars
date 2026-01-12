const merryChristmas = funcs => {
  const ret = [];
  const strng = "Merry Christmas!";
  for (const chr of strng) {
    for (const f of funcs) {
      if (f() === chr) {
        ret.push(f.name);
      }
    }
  }
  return ret.join(",");
};
