#include <cctype>
#include <random>
#include <string>

std::string randomCase(std::string x) {
    std::random_device rand_dev;
    std::mt19937 mtgen(rand_dev());
    std::uniform_int_distribution<int> dist(0, 1);
    for (unsigned i = 0; i < x.size(); i++) {
        if (std::isupper(x[i])) {
            if (dist(mtgen)) {
                x[i] = std::tolower(x[i]);
            }
        }
        else {
            if (dist(mtgen)) { 
                x[i] = std::toupper(x[i]);
            }
        }
    }
    return x;
}