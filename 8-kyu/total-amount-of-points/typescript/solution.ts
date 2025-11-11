export const points = (games: string[]): number => {
  return games.map((game: string): number => {
    const [ ownScore, oppScore ] = game.split(":").map(Number);
    if (ownScore > oppScore) {
      return 3;
    } else if (ownScore === oppScore) {
      return 1;
    }
    return 0;
  }).reduce((acc, nxt) => acc + nxt, 0);
};