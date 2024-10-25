class Ship {
  constructor(draft, crew) {
    this.draft = draft;
    this.crew = crew;
  }
  
  isWorthIt() {
    const weightMinusCrew = this.draft - this.crew * 1.5;
    return weightMinusCrew > 20;
  }
}
