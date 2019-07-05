#include <cmath>

std::vector<bool> make_prime_sieve()
{
    auto ret = std::vector<bool>(1000000, true);
    ret[0] = false;
    ret[1] = false;
    for (unsigned i = 2; i < 1000000; i++) {
        if (ret[i]) {
            for (unsigned j = i * i; j < std::sqrt(1000000); j += i) {
                ret[j] = false;
            }
        }
    }
    return ret;
}

std::vector<int> prime_word(const std::vector<std::pair<std::string, int>> &list)
{
    auto primes = make_prime_sieve();
    std::vector<int> ret;
    for (const auto &pair : list) {
        bool contains_prime = false;
        for (const auto &c : pair.first) {
            int check_for_prime = static_cast<int>(c) + pair.second;
            if (primes[check_for_prime]) {
                contains_prime = true;
                break;
            }
        }
        if (contains_prime) ret.push_back(1);
        else ret.push_back(0);
    }
    return ret;
}