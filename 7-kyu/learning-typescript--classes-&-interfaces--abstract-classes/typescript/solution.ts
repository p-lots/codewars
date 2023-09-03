export abstract class Animal {
  /** @param {number} value The length of the animal in parrots. */
  protected constructor(public value: number) {}

  convertTo (someone: Animal): number {
    return this.value;
  }
}

/*
  1 boa = 38 parrots = 5 monkeys, therefore:
  1 parrot = 1/38 (in terms of boa) = 5/38 (in terms of monkey)
  1 monkey = 1/5 (in terms of boa) = 38/5 (in terms of parrot)
 */

export class Boa extends Animal {
  constructor() {
    super(1);
  }
  
  convertTo(someone: Animal): number {
    if (someone instanceof Monkey) {
      return 5 / this.value;
    } else if (someone instanceof Parrot) {
      return 38 / this.value;
    }
    return this.value;
  }
}

export class Parrot extends Animal {
  constructor() {
    super(38);
  }
  
  convertTo(someone: Animal): number {
    if (someone instanceof Monkey) {
      return 5 / this.value;
    } else if (someone instanceof Boa) {
      return 1 / this.value;
    }
    return this.value;
  }
}

export class Monkey extends Animal {
  constructor() {
    super(5);
  }
  
  convertTo(someone: Animal): number {
    if (someone instanceof Boa) {
      return 1 / this.value;
    } else if (someone instanceof Parrot) {
      return 38 / this.value;
    }
    return this.value;
  }
}
