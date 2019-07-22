import Foundation

func findNb(_ number: Int) -> Int {
    var ret = 0, nb = number
    while true {
        ret += 1
        nb -= Int(pow(Double(ret), 3.0))
        if nb == 0 { return ret }
        else if nb < 0 { return -1 }
    }
}