#include <array>
#include <string>

int points(const std::array<std::string, 10>& games) {
    int ret = 0;
    for (const std::string &score : games) {
        auto colon_pos = score.find(':');
        auto x_score_str = score.substr(0, colon_pos);
        auto y_score_str = score.substr(colon_pos + 1);
        auto x_score = std::stoi(x_score_str);
        auto y_score = std::stoi(y_score_str);
        ret += (x_score > y_score ? 3 : x_score == y_score ? 1 : 0);
    }
    return ret;
}