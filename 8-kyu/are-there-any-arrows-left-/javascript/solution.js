const anyArrows = (arrows) => {
  return arrows.some(quiver => quiver.hasOwnProperty("damaged") ? quiver.damaged === false : true);
};
