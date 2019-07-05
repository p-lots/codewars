#include <vector>

std::string how_much_i_love_you(int nb_petals) {
    std::vector<std::string> phrases = {
        "I love you",
        "a little",
        "a lot",
        "passionately",
        "madly",
        "not at all"
    };
    int counter = 1, at = 0;
    while (counter < nb_petals) {
        counter++;
        at++;
        if (at > 5) at = 0;
    }
    return phrases.at(at);
}