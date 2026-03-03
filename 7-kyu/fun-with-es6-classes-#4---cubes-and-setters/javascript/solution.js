class Cube {
  constructor(_length) {
    this.length = _length;
  }
  set surfaceArea(_surfaceArea) {
    this.length = Math.sqrt(_surfaceArea / 6);
  }
  get surfaceArea() {
    return 6 * this.length ** 2;
  }
  set volume(_volume) {
    this.length = _volume ** (1 / 3);
  }
  get volume() {
    return this.length ** 3;
  }
};