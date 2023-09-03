# Learning TypeScript. Classes & Interfaces. Abstract classes

## Overview

Abstract classes are base classes from which other classes may be derived. They may not be instantiated directly. Unlike an interface, an abstract class may contain implementation details for its members. The <code>abstract</code> keyword is used to define abstract classes as well as abstract methods within an abstract class.

```typescript
abstract class Animal {
    abstract makeSound(): void;
    move(): void {
        console.log("roaming the earth...");
    }
}
```

Methods within an abstract class that are marked as abstract do not contain an implementation and must be implemented in derived classes. Abstract methods share a similar syntax to interface methods. Both define the signature of a method without including a method body. However, abstract methods must include the abstract keyword and may optionally include access modifiers.

```typescript
abstract class Department {
    constructor(public name: string) {}

    printName(): void {
        console.log("Department name: " + this.name);
    }

    abstract printMeeting(): void; // must be implemented in derived classes
}

class AccountingDepartment extends Department {
    constructor() {
        super("Accounting and Auditing"); // constructors in derived classes must call super()
    }

    printMeeting(): void {
        console.log("The Accounting Department meets each Monday at 10am.");
    }

    generateReports(): void {
        console.log("Generating accounting reports...");
    }
}

let department: Department; // ok to create a reference to an abstract type
department = new Department(); // error: cannot create an instance of an abstract class
department = new AccountingDepartment(); // ok to create and assign a non-abstract subclass
department.printName();
department.printMeeting();
department.generateReports(); // error: method doesn't exist on declared abstract type

```

## Task

There is an old funny USSR's cartoon called "38 parrots" (https://www.youtube.com/watch?v=iEHyrNX4IR8 - with English subtitles).
In this cartoon monkey and parrot measured boa... and they found out that one boa is equal to 38 parrots or 5 monkeys.

You're given an abstract class <code>Animal</code> and stubs for classes <code>Animal</code>, <code>Boa</code>, <code>Parrot</code> and <code>Monkey</code>:

```typescript
export abstract class Animal {
  /** @param {number} value The length of the animal in parrots. */
  protected constructor(public value: number) {}

  convertTo (someone: Animal) {
    // TODO:
  }
}

export class Boa extends Animal {
  // TODO:
}

export class Parrot extends Animal {
  // TODO:
}

export class Monkey extends Animal {
  // TODO:
}
```

Your task is to implement these classes. <code>Boa</code>, <code>Parrot</code> and <code>Monkey</code> must convert to each other correctly. 

Have fun! )


**P.S.** Solved this kata? Take a look at other katas in "<a href="https://www.codewars.com/collections/learning-typescript">Learning TypeScript</a>" collection.