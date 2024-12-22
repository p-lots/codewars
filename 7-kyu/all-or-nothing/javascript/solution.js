const possiblyPerfect = (key, answers) => {
  return key.every((val, idx) => val === "_" ? true : val === answers[idx])
    || key.every((val, idx) => val === "_" ? true : val !== answers[idx]);
};
