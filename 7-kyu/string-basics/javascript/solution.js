const getUsersIds = (str) => {
  let rawStr = str.trim();
  while (rawStr.indexOf("#") !== -1) {
   rawStr = rawStr.replace("#", "");
  }
  const rawSplit = rawStr.split(", ");
  const uids = rawSplit.map(s => s.replace("uid", "").toLowerCase().trim());
  return uids;
};
