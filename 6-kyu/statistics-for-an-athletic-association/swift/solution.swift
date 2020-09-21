import Foundation

func stat(_ strg: String) -> String {
    guard !strg.isEmpty else { return String() }
    let timesArr = strg.components(separatedBy: ",")
    let secondsArr = timesArr.map { (timecode: String) -> Int in 
        let timecodeSplit = timecode.components(separatedBy: "|")
        var hours = 0, minutes = 0, seconds = 0
        if let hoursFromArr = Int(timecodeSplit[0]) {
            hours = hoursFromArr * 60 * 60
        }
        if let minutesFromArr = Int(timecodeSplit[1]) {
            minutes = minutesFromArr * 60
        }
        if let secondsFromArr = Int(timecodeSplit[2]) {
            seconds = secondsFromArr
        }
        return hours + minutes + seconds
    }.sorted()
    let range = getRange(secondsArr)
    let average = Int(getAverage(secondsArr))
    let median = getMedian(secondsArr)
    return "Range: \(format(range)) Average: \(format(average)) Median: \(format(median))"
}

func getRange(_ arr: [Int]) -> Int {
    if let min = arr.min(), let max = arr.max() {
        return max - min
    }
    return 0
}

func getAverage(_ arr: [Int]) -> Double {
    return Double(arr.reduce(0, +)) / Double(arr.count)
}

func getMedian(_ arr: [Int]) -> Int {
    let mid = arr.count / 2
    return arr.count % 2 == 1 ? arr[mid] : ((arr[mid - 1] + arr[mid]) / 2)
}

func format(_ secs: Int) -> String {
    let hours = secs / (60 * 60)
    let minutes = secs % (60 * 60) / 60
    let seconds = secs % (60 * 60) % 60
    return String(format: "%02d|%02d|%02d", hours, minutes, seconds)
}
