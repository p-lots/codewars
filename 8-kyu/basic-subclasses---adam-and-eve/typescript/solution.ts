export class God {
/**
 * @returns Human[]
 */
  static create(): Human[] {
    const adam = new Man();
    const eve = new Woman();
    return [adam, eve];
  }
}

export class Human { }

export class Man extends Human { }

export class Woman extends Human { }