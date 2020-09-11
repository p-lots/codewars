func replaceAll<T: Equatable>(array: [T], old: T, new: T) -> [T] {
    return array.map { $0 == old ? new : $0 }
}