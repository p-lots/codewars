func flyBy(lamps: String, drone: String) -> String {
    let lampsCount = lamps.count
    let droneCount = drone.count
    let oRepeatCount = droneCount > lampsCount ? droneCount - 1 : droneCount
    let xRepeatCount = max(min(lampsCount - droneCount, lampsCount), 0)
    return "\(String(repeating: "o", count: oRepeatCount))\(String(repeating: "x", count: xRepeatCount))"
}