const anchorize = text => {
  const urlRegexp = /(http[s]?|ftp[s]?|file|smb)(:\/\/[a-z]+:?(\.[a-z]{3})?(\/[a-z]+\.[a-z]{3})?)/gi;
  const anchorText = text.replaceAll(urlRegexp, '<a href="$1$2">$1$2</a>');
  return anchorText;
};
