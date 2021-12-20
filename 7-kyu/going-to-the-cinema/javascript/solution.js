const movie = (card, ticket, perc) => {
  let ret = 1;
  let card_price = card + ticket * perc;
  let total_ticket = ticket;
  while (!(total_ticket > Math.ceil(card_price))) {
    ret += 1;
    card_price += ticket * Math.pow(perc, ret);
    total_ticket += ticket
  }
  return ret;
};