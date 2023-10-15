function isInStrictMode() {
  var strict = true;
  eval("var strict = false;");
  return strict;
}