const last = (...args) => {
  if (args.length === 1) {
    try {
      return args.at(-1).at(-1);
    } catch {
      return args[0];
    }
  }
  return args.at(-1);
};
