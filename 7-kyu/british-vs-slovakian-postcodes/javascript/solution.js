const whichPostcode = postcode => {
  const gbRegexp = /^[a-z]{1,2}[0-9]{1,2} [0-9][a-z]{2}$/gi;
  const skRegexp = /^[0-9]{3} [0-9]{2}$/g;
  const postcodeTrimmed = postcode.trim();
  if (gbRegexp.test(postcodeTrimmed)) {
    return "GB";
  } else if (skRegexp.test(postcodeTrimmed)) {
    return "SK";
  }
  return "Not valid";
};
