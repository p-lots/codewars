func bmi(_ weight: Int, _ height: Double) -> String {
    let bmi = Double(weight) / (height * height)
    return bmi <= 18.5 ? "Underweight"
        : bmi <= 25.0 ? "Normal"
            : bmi <= 30.0 ? "Overweight"
                : "Obese"
}