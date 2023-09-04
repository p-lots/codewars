export class Cuboid {
  length: number;
  width: number;
  height: number;
  
  constructor(l: number, w: number, h: number) {
    this.length = l;
    this.width = w;
    this.height = h;
  }
  
  get surfaceArea(): number {
    return 2 * (this.length * this.width + this.width * this.height + this.height * this.length);
  }
  
  get volume(): number {
    return this.length * this.height * this.width;
  }
}

export class Cube extends Cuboid {
  constructor(sideLength: number) {
    super(sideLength, sideLength, sideLength);
  }
}
