import Foundation

func mean(_ d: String, _ town: String) -> Double {
    let dataDict = prepareDict(d)
    guard let townArray = dataDict[town] else { return -1.0 }
    return Double(townArray.reduce(0.0, +)) / Double(townArray.count)
}

func variance(_ d: String, _ town: String) -> Double {
    let dataDict = prepareDict(d)
    guard let townArray = dataDict[town] else { return -1.0 }
    let avg = Double(townArray.reduce(0.0, +)) / Double(townArray.count)
    let differencesSquared = townArray.map { (temp: Double) -> Double in let diff = temp - avg; return diff * diff }
    return Double(differencesSquared.reduce(0.0, +)) / Double(differencesSquared.count)
}

func prepareDict(_ data: String) -> [String: [Double]] {
    let lines = data.components(separatedBy: "\n")
    var ret: [String: [Double]] = [:]
    let _ = lines.forEach { line in
        let dataSplitOnColon = line.components(separatedBy: ":")
        let cityName = dataSplitOnColon[0]
        ret[cityName] = dataSplitOnColon[1].components(separatedBy: ",").map { item -> Double in
            let itemSplit = item.components(separatedBy: " ")
            return Double(itemSplit[1]) ?? 0.0
        }
    }
    return ret
}