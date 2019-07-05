extension String {
    func containsIgnoreCase(_ find: String) -> Bool{
       return self.lowercased().range(of: find.lowercased()) != nil
     }
}

func wordSearch(_ str:String, _ arr:[String]) -> [String] {
    let ret : [String] = arr.filter { $0.containsIgnoreCase(str) }
    return ret.isEmpty ? ["Empty"] : ret
}

