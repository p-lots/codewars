func movie(card: Double, ticket: Double, perc: Double) -> Int {
    var ret = 1
    var card_price: Double = card + ticket * perc
    var total_ticket = Int(ticket)
    while !(Int(ceil(card_price)) < total_ticket) {
        ret += 1
        card_price += ticket * (pow(perc, Double(ret)))
        total_ticket += Int(ticket)
    }
    return ret
}
