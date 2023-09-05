declare var ICuboid: {
  new (length: number): ICuboid;
}

interface ICuboid {
  /** Length of the cube */
  length: number;
  /** Surface area of the cube */
  surfaceArea: number;
  /** Volume of the cube */
  volume: number;
}

export class Cube implements ICuboid {
  public length: number;
  
  constructor(length: number) {
    this.length = length;
  }
  get surfaceArea(): number {
    return this.length ** 2 * 6;
  }
  set surfaceArea(givenSurfaceArea: number) {
    this.length = (givenSurfaceArea / 6) ** 0.5;
  }
  get volume(): number {
    return this.length ** 3;
  }
  set volume(givenVolume: number) {
    this.length = givenVolume ** (1 / 3);
  }
}