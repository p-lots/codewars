import Foundation

func correct(_ timeString: String?) -> String? {
  guard let timeString = timeString else { return nil }
  if timeString.isEmpty {
    return ""
  }
  let timeSplit = timeString.components(separatedBy: ":").compactMap { Int($0) }
  if timeSplit.count != 3 {
    return nil
  }
  let totalSeconds = timeSplit[0] * 3600 + timeSplit[1] * 60 + timeSplit[2]
  let hours = totalSeconds / 3600 % 24
  let minutes = totalSeconds / 60 % 60
  let seconds = totalSeconds % 60
  return String(format: "%02d:%02d:%02d", hours, minutes, seconds)
}