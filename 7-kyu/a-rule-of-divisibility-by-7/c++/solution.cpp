#include <cmath>
#include <utility>

typedef long long ll;

class DivSeven
{
public:
    static std::pair <ll, ll> seven(ll m);
};

std::pair <ll, ll> DivSeven::seven(ll m)
{
    ll steps = 0;
    while (std::log10(m) > 2) {
        m = (m / 10) - ((m % 10) * 2);
        steps++;
    }
    return std::make_pair(m, steps);
}