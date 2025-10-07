const validate = (username, password) => {
  if (/[|/]{2}/.test(password)) {
    return "Wrong username or password!";
  }
  var database = new Database();
  return database.login(username, password);
};
