const cookie = x => {
  let who;
  switch (typeof x) {
    case "string":
      who = "Zach";
      break;
    case "number":
      who = "Monica";
      break;
    default:
      who = "the dog";
      break;
  }
  return `Who ate the last cookie? It was ${who}!`;
};
