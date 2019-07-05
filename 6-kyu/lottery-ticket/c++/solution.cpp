std::string bingo(std::vector<std::pair<std::string, int>> ticket, int win)
{
    int wins_on_ticket = 0;
    for (const auto &pair : ticket) {
        auto char_code = pair.second;
        for (const auto &ch : pair.first) {
            if (static_cast<int>(ch) == char_code) {
                wins_on_ticket++;
                break;
            }
        }
    }
    return wins_on_ticket >= win ? "Winner!" : "Loser!";
}