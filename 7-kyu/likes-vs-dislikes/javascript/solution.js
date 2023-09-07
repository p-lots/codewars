// Like, Dislike, Nothing come from Preloaded

const likeOrDislike = (buttons) => {
  let current = Nothing;
  for (const press of buttons) {
    current = press === current ? Nothing : press;
  }
  return current;
};
