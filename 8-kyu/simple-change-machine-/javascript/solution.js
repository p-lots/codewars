const changeMe = moneyIn => {
  switch (moneyIn) {
      case "£5":
      return ("20p ".repeat(25)).slice(0, -1);
      case "£2":
      return ("20p ".repeat(10)).slice(0, -1);
      case "£1":
      return ("20p ".repeat(5)).slice(0, -1);
      case "50p":
      return "20p 20p 10p";
      case "20p":
      return "10p 10p";
      default:
      return moneyIn;
  }
}