const montyHall = (correctDoorNumber, participantGuesses) => {
  const loseCount = participantGuesses.length - participantGuesses.filter((elem) => elem === correctDoorNumber).length;
  return Math.round(loseCount / participantGuesses.length * 100.0);
};
