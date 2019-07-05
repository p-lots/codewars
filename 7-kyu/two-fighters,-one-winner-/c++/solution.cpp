std::string declareWinner(Fighter* fighter1, Fighter* fighter2, std::string firstAttacker)
{
    std::string ret;
    int f1_current = fighter1->getHealth(), f2_current = fighter2->getHealth();
    int f1_attack = fighter1->getDamagePerAttack(), f2_attack = fighter2->getDamagePerAttack();
    if (fighter1->getName() == firstAttacker) {
        while (true) {
            f2_current -= f1_attack;
            fighter2->setHealth(f2_current);
            if (fighter2->getHealth() <= 0) {
                ret = fighter1->getName();
                break;
            }
            f1_current -= f2_attack;
            fighter1->setHealth(f1_current);
            if (fighter1->getHealth() <= 0) {
                ret = fighter2->getName();
                break;
            }
        }
    }
    else if (fighter2->getName() == firstAttacker) {
        while (true) {
            f1_current -= f2_attack;
            fighter1->setHealth(f1_current);
            if (fighter1->getHealth() <= 0) {
                ret = fighter2->getName();
                break;
            }
            f2_current -= f1_attack;
            fighter2->setHealth(f2_current);
            if (fighter2->getHealth() <= 0) {
                ret = fighter1->getName();
                break;
            }
        }
    }
    return ret;
}