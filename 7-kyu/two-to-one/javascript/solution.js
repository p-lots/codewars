class TwoToOne
{
public:
    static std::string longest(const std::string &s1, const std::string &s2)
    {
        auto sorted_a = s1, sorted_b = s2;
        std::sort(sorted_a.begin(), sorted_a.end());
        std::sort(sorted_b.begin(), sorted_b.end());
        auto a_it = std::unique(sorted_a.begin(), sorted_a.end());
        sorted_a.erase(a_it, sorted_a.end());
        auto b_it = std::unique(sorted_b.begin(), sorted_b.end());
        sorted_b.erase(b_it, sorted_b.end());
        std::string ret;
        ret.insert(ret.end(), sorted_a.begin(), sorted_a.end());
        ret.insert(ret.end(), sorted_b.begin(), sorted_b.end());
        std::sort(ret.begin(), ret.end());
        auto ret_it = std::unique(ret.begin(), ret.end());
        ret.erase(ret_it, ret.end());
        return ret;
    }
};