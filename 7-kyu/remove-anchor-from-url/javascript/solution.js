const removeUrlAnchor = (url) => {
  const anchorIdx = url.indexOf("#");
  if (anchorIdx === -1) {
    return url;
  }
  return url.slice(0, anchorIdx);
};
