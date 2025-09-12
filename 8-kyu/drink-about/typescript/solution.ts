export const peopleWithAgeDrink = (old: number): string => {
  let drink: string = "";
  if (old >= 21) {
    drink = "whisky";
  } else if (old > 17) {
    drink = "beer";
  } else if (old > 13) {
    drink = "coke";
  } else {
    drink = "toddy";
  }
  return `drink ${drink}`;
}
