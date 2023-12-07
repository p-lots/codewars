func merge<Key, Value>(_ dicts: [[Key: Value]]) -> [Key: [Value]] {
  var ret = [Key: [Value]]()
  for dict in dicts {
    for (key, val) in dict {
      var valsArr = [Value]()
      if let valArrayFromRet = ret[key] {
        valsArr = valArrayFromRet
        valsArr.append(val)
        ret.updateValue(valsArr, forKey: key)
      }
      else {
        valsArr.append(val)
        ret.updateValue(valsArr, forKey: key)
      }
    }
  }
  return ret
}