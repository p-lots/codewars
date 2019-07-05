// Define the "Ball" class here
class Ball {
    var type: String
    init() {
        self.type = "regular"
    }
    init(type typeName: String) {
        self.type = typeName
    }
}