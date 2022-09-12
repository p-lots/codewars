class Person {
  constructor(first = "John", last = "Doe", age = 0, gender = "Male") {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.gender = gender;
  }
  sayFullName() {
    return `${this.firstName} ${this.lastName}`;
  }
  static greetExtraTerrestrials(raceName) {
    return `Welcome to Planet Earth ${raceName}`;
  }
}
