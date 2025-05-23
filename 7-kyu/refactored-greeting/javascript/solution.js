class Person {
  constructor(name) {
    this.name = name;
  }
  
  greet(otherName) {
    return `Hello ${otherName}, my name is ${this.name}`;
  }
}
