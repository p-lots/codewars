class God {
/**
 * @returns Human[]
 */
  static create() {
    const adam = new Man();
    const eve = new Woman();
    return [adam, eve];
  }
}

class Human { }

class Man extends Human { }

class Woman extends Human { }