const generateLink = user => {
  const baseURL = "http://www.codewars.com/users/";
  return `${baseURL}${encodeURIComponent(user)}`;
};
