extension Int {
    var array : [Int] {
        return description.characters.flatMap{Int(String($0))}
    }
}

func descendingOrder(of number: Int) -> Int {
    let num_arr = number.array
    let num_arr_sorted = num_arr.sorted {$0 < $1}
    var ret = 0
    var mult = 1
    num_arr_sorted.forEach {
        ret += mult * $0
        mult *= 10
    }
    return ret
}