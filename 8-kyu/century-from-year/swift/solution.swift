import Foundation

func century(_ year: Int) -> Int {
    var century: Double = Double(year) / 100.0
    century.round(.up)
    return Int(century)
}