func RentalCarCost(_ days: Int) -> Int {
    let total : Int = days * 40
    return days >= 7 ? total - 70 : days >= 3 ? total - 20 : total
}