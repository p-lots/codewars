func persistence(for num: Int) -> Int {
   var ret = 0
   var num_str = String(num)
   while num_str.characters.count > 1 {
       var sum = 1
       for c in num_str.characters {
           let temp = String(c)
           if let temp_int = Int(temp) {
               sum *= temp_int
           }
       }
       ret += 1
       num_str = String(sum)
   }
   return ret
}