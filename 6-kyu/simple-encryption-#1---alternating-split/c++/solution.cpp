std::string encrypt(std::string text, int n)
{
    if (n <= 0 || text.empty()) return text;
    std::string ret = text;
    while (n--) {
        std::string p1 = "", p2 = "";
        for (unsigned i = 1; i < ret.length(); i += 2) {
            p1.push_back(ret[i]);
        }
        for (unsigned i = 0; i < ret.length(); i += 2) {
            p2.push_back(ret[i]);
        }
        ret = p1 + p2;
    }
    return ret;
}

std::string decrypt(std::string encryptedText, int n)
{
    if (n <= 0 || encryptedText.empty()) return encryptedText;
    std::string ret = encryptedText;
    while (n--) {
        std::string p1 = ret.substr(0, ret.length() / 2);
        std::string p2 = ret.substr(ret.length() / 2);
        auto p2_it = p2.begin();
        auto p1_it = p1.begin();
        std::string temp = "";
        while (p1_it != p1.end()) {
            temp.push_back(*p2_it);
            temp.push_back(*p1_it);
            p2_it++;
            p1_it++;
        }
        if (p1.length() != p2.length()) {
            temp.push_back(p2.back());
        }
        ret = temp;
    }
    return ret;
}