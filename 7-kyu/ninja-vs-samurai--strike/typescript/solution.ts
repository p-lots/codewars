export class Warrior {
  private name: string;
	public health: number;
  public strike: Function;
  constructor(name: string){
    this.name = name;
    this.health = 100;
    this.strike = function(enemy: Warrior, swings: number) {
      enemy.health = Math.max(0, enemy.health - (swings * 10));
    }
  }
}