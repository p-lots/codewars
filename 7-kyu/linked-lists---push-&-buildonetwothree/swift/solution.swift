class Node {
    var data: Int
    var next: Node?
    
    init(_ data: Int) {
        self.data = data;
    }
}

func push(_ head:Node?, _ data:Int) -> Node {
    guard head != nil else { return Node(data) }
    var first = Node(data)
    first.next = head
    return first
}

func buildOneTwoThree() -> Node {
    var ret = Node(3)
    ret = push(ret, 2)
    ret = push(ret, 1)
    return ret
}