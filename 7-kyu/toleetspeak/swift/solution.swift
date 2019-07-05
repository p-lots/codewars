func toLeetSpeak(_ s : String) -> String {
    return String(s.characters.map { leetSpeakLookup($0) })
}

func leetSpeakLookup(_ c : Character) -> Character {
    switch(c) {
        case "A": return "@"
        case "B": return "8"
        case "C": return "("
        case "D": return "D"
        case "E": return "3"
        case "F": return "F"
        case "G": return "6"
        case "H": return "#"
        case "I": return "!"
        case "J": return "J"
        case "K": return "K"
        case "L": return "1"
        case "M": return "M"
        case "N": return "N"
        case "O": return "0"
        case "P": return "P"
        case "Q": return "Q"
        case "R": return "R"
        case "S": return "$"
        case "T": return "7"
        case "U": return "U"
        case "V": return "V"
        case "W": return "W"
        case "X": return "X"
        case "Y": return "Y"
        case "Z": return "2"
        default: return c
    }
}