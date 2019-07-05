infix operator ?=
extension Int {
    static func ?=(left: Int, right: Int) -> Bool {
        let lower : Int = Int(Double(left) * 0.9), higher : Int = Int(Double(left) * 1.1)
        return right > lower && right < higher
    }
}

extension Double {
    static func ?=(left: Double, right: Double) -> Bool {
        let lower : Double = left * 0.9, higher : Double = left * 1.1
        return right > lower && right < higher
    }
}

extension Float {
    static func ?=(left: Float, right: Float) -> Bool {
        let lower : Float = left * Float(0.9), higher : Float = left * Float(1.1)
        return right > lower && right < higher
    }
}