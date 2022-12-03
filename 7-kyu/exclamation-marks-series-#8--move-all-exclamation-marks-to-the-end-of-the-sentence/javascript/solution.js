const remove = s => {
  const noExclamation = s.replace(/!/ig, "");
  return `${noExclamation}${"!".repeat(s.length - noExclamation.length)}`;
};
