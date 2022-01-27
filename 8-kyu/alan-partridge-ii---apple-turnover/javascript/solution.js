const apple = x => {
  if (typeof x === 'string') {
    x = parseInt(x);
  }
  return x * x > 1000 ? "It's hotter than the sun!!" : "Help yourself to a honeycomb Yorkie for the glovebox.";
}