const encryption = message => {
  return message.split("")
    .map(ch => ch === " " ? " " : CHAR_TO_MORSE[ch])
    .join(" ");
};
