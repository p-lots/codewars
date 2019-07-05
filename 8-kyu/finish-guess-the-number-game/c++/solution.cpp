#include <stdexcept>

class Guesser
{
public:
    Guesser(int number, int lives)
      : number(number), lives(lives)
    { }
    bool guess(int n)
    {
        if (lives == 0) throw std::exception();
        else if (n != number) {
            lives -= 1;
            return false;
        }
        return true;
    }
private:
    int number, lives;
};