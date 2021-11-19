class Node {
    var data: Int
    var next: Node?
    init(_ data: Int) {
        self.data = data
    }
}

func length(_ head: Node?) -> Int {
    guard let node = head else { return 0 }
    return 1 + length(node.next)
}

func count(_ head: Node?, _ data: Int) -> Int {
    var ret: Int = 0
    guard let node = head else { return ret }
    if node.data == data {
        ret = 1
    }
    return ret + count(node.next, data)
}