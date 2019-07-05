import Foundation

func accum(_ s: String) -> String {
  var i = 0
  let arr: [String] = s.characters.flatMap { ret in
    i += 1
    return String(repeating: String(ret).lowercased(), count: i) }
  return arr.joined(separator: "-").capitalized
}