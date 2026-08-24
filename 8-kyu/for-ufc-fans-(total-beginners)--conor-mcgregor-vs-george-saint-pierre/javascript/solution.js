const quote = fighter => {
  const lowered = fighter.toLowerCase();
  const responses = {
    "george saint pierre": "I am not impressed by your performance.",
    "conor mcgregor": "I'd like to take this chance to apologize.. To absolutely NOBODY!"
  };
  return responses[lowered];
};