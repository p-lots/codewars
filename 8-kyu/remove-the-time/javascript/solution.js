const shortenToDate = longDate => {
  const commaIdx = longDate.indexOf(",");
  const timeOmitted = longDate.slice(0, commaIdx);
  return timeOmitted;
};
