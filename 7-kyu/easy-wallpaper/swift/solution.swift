

func wallpaper(_ l: Double, _  w: Double,_  h: Double) -> String {
    let numbers = ["zero", "one", "two", "three", "four", "five",
               "six", "seven", "eight", "nine", "ten",
               "eleven", "twelve", "thirteen", "fourteen", "fifteen",
               "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    guard l > 0.0 && w > 0.0 && h > 0.0 else { return numbers[0] }
    var result: Double = ((2.0 * w * h) + (2.0 * h * l)) * 1.15 / 5.2
    result.round(.up)
    let index = Int(result)
    return numbers[index]
}