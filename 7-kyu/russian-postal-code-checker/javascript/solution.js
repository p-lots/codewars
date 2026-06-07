const zipvalidate = postcode => {
  const regex = /^([1-4]|6)\d{5}$/;
  return regex.test(postcode);
};
