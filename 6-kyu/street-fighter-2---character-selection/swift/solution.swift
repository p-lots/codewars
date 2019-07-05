func streetFighterSelection(fighters: [[String]], position: (row: Int, column: Int), moves: [Direction]) -> [String] {
  var ret = [String]()
  var currentPosition = position
  for move in moves {
      switch move {
          case .up:
          if currentPosition.row == 1 {
              currentPosition.row -= 1
          }
          case .down:
          if currentPosition.row == 0 {
              currentPosition.row += 1
          }
          case .left:
          currentPosition.column -= 1
          if currentPosition.column < 0 {
              currentPosition.column += 6
          }
          case .right:
          currentPosition.column = (currentPosition.column + 1) % 6
      }
      ret.append(fighters[currentPosition.row][currentPosition.column])
  }
  return ret
}