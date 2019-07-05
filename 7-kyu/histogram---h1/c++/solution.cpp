std::string histogram(std::vector<int> results)
{
    std::string ret = "";
    int curr_side = 6;
    for (auto r_it = results.rbegin(); r_it != results.rend(); r_it++) {
        std::string line = std::to_string(curr_side) + "|";
        if (*r_it == 0) {
            line += "\n";
            ret += line;
            curr_side--;
            continue;
        }
        line += std::string(*r_it, '#') + " " + std::to_string(*r_it) + "\n";
        ret += line;
        curr_side--;
    }
    return ret;
}