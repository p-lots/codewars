import Foundation

func calculate1RM(_ weight: Int, _ reps: Int) -> Int? {
    if reps == 0 {
        return nil
    }
    else if reps == 1 {
        return weight
    }
    let epley = Double(weight) * (1 + Double(reps) / 30)
    let mcglothin = 100 * Double(weight) / (101.3 - 2.67123 * Double(reps))
    let lombardi = Double(weight) * pow(Double(reps), 0.1)
    let results: [Double] = [epley.rounded(), mcglothin.rounded(), lombardi.rounded()]
    return Int(results.max()!)
}