const testit = s => {
  return s.match(/w.*?o.*?r.*?d/gi)?.length ?? 0;
};
