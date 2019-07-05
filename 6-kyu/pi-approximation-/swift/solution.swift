import Foundation

func iterPi(_ epsilon: Double) -> (Int, String) {
    var iterCount: Int = 0
    var calcPi: Double = 0.0
    var denominator: Double = 1.0
    while (abs(Double.pi - calcPi * 4.0) > epsilon) {
        if (iterCount % 2 == 0) {
            calcPi += 1.0 / denominator
        }
        else {
            calcPi -= 1.0 / denominator
        }
        denominator += 2.0
        iterCount += 1
    }
    return (iterCount, String(format: "%.10f", calcPi * 4.0))
}