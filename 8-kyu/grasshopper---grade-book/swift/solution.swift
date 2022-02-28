func getGrade(_ s1: Int, _ s2: Int, _ s3: Int) -> String {
  let grades = [s1, s2, s3]
  let average = grades.reduce(0, +) / grades.count
  switch average {
    case 90...100:
    return "A"
    case 80...89:
    return "B"
    case 70...79:
    return "C"
    case 60...69:
    return "D"
    default:
    return "F"
  }
}