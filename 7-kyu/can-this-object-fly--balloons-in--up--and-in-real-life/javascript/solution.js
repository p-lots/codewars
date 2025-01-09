class Journey {
  constructor(object, crew, balloons) {
    this.weight = object.weight;
    this.crew = crew;
    this.balloons = balloons;
  }
  isPossible() {
    return this.weight + this.crew * 80 <= this.balloons * 0.0048;
  }
}
