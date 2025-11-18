export const well = (x: string[]): string => {
  const goodCount = x.filter(idea => idea === "good").length;
  if (goodCount > 2) {
    return "I smell a series!";
  } else if (goodCount > 0) {
    return "Publish!";
  }
  return "Fail!";
};
