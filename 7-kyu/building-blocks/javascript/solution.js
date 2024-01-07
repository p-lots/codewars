class Block {

  constructor(data) {
    const [width, length, height] = data;
    this.width = width;
    this.length = length;
    this.height = height;
  }
  
  getWidth() {
    return this.width;
  }
  
  getLength() {
    return this.length;
  }
  
  getHeight() {
    return this.height;
  }
  
  getVolume() {
    return this.length * this.width * this.height;
  }
  
  getSurfaceArea() {
    return 2 * (this.length * this.height + this.height * this.width +
      this.length * this.width);
  }
  
}