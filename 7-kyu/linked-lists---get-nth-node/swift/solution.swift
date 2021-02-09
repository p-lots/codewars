class Node {
    var data: Int
    var next: Node?
    init(_ data: Int) {
        self.data = data
    }
}

enum LinkedListError: Error {
    case InvalidArgument
}

func getNth(_ head: Node?, _ index: Int) throws -> Node? {
    guard var curr = head else { throw LinkedListError.InvalidArgument }
    guard index >= 0 else { throw LinkedListError.InvalidArgument }
    var i: Int = 0
    while i < index {
        if let next = curr.next {
            i += 1
            curr = next
        } else {
            throw LinkedListError.InvalidArgument
        }
    }
    return curr
}
