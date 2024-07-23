const areYouPlayingBanjo = name => {
  const interpString = name[0].toLowerCase() === 'r' ? "plays" : "does not play";
  return `${name} ${interpString} banjo`;
};
