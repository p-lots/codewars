func warnTheSheep(_ queue: [String]) -> String {
    let wolfIdx = queue.firstIndex(of: "wolf")!
    return wolfIdx == queue.count - 1 ? "Pls go away and stop eating my sheep" : "Oi! Sheep number \(queue.count - wolfIdx - 1)! You are about to be eaten by a wolf!"
}