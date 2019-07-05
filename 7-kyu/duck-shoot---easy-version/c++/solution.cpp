#include <cmath>
#include <string>

std::string duckShoot(int ammo, double aim, std::string ducks)
{
    int ducksShot = std::floor(static_cast<double>(ammo) * aim);
    for (auto &c : ducks) {
        if (c == '2' && ducksShot > 0) {
            c = 'X';
            ducksShot--;
        }
    }
    return ducks;
}