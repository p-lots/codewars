const caffeineBuzz = n => {
  let script = "";
  if (n % 12 === 0) {
    return "CoffeeScript";
  } else if (n % 3 === 0) {
    script = "Java"; 
  } else {
    script = "mocha_missing!";
  }
  if (n % 6 === 0) {
    script += "Script";
  }
  return script;
}