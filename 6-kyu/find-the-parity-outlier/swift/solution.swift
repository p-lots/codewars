import Foundation

func findOutlier(_ array: [Int]) -> Int {
    let noEvens = array.filter { abs($0) % 2 == 1 }
    if noEvens.count == 1 { return noEvens[0] }
    else {
        let noOdds = array.filter { abs($0) % 2 == 0 }
        return noOdds[0]
    }
}