func toArray(_ number: Int) -> [Int] {
	guard number != 0 else { return [0] }
	var n = number
	if (n < 0) {
		n *= -1
	}
	var ret = [Int]()
	while (n > 0) {
		ret.append(n % 10)
		n /= 10
	}
	return ret.reversed()
}

func dashatize(_ number: Int) -> String {
	var ret = String()
	var numArr = toArray(number)
	guard numArr.count > 1 else { return String(numArr[0]) }
	var prevWasOdd = false
	for i in 0..<numArr.count {
		if (numArr[i] % 2 == 0) {
			ret += String(numArr[i])
			prevWasOdd = false
			continue
		}
		if (i == 0) {
			ret += String(String(numArr[i]) + "-")
		}
		else if (i == numArr.count - 1) {
			if (prevWasOdd) {
				ret += String(numArr[i])
			}
			else {
				ret += String("-" + String(numArr[i]))
			}
		}
		else {
			if (prevWasOdd) {
				ret += String(String(numArr[i]) + "-")
			}
			else {
				ret += String("-" + String(numArr[i]) + "-")
			}
		}
		prevWasOdd = true
	}
	return ret
}