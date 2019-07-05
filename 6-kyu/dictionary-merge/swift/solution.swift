func merge<Key, Value>(_ dicts: [[Key: Value]]) -> [Key: [Value]] {
    var ret = [Key: [Value]]()
    for dict in dicts {
        for (key, val) in dict {
            var valsArr = ret[key] ?? [Value]()
            valsArr.append(val)
            ret.updateValue(valsArr, forKey: key)
        }
    }
    return ret
}