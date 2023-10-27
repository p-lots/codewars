class Quark {
  constructor(color, flavor) {
    this.flavor = flavor;
    this.color = color;
    this.baryon_number = 1 / 3;
  }
  
  interact(other) {
    const tempColor = this.color;
    this.color = other.color;
    other.color = tempColor;
  }
}