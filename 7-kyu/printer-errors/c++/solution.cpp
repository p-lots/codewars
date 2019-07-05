class Printer
{
public:
    static std::string printerError(const std::string &s);
};

std::string Printer::printerError(const std::string &s)
{
    unsigned len = s.length(), num_wrong = 0;
    for (const auto c : s) {
        if (c > 'm') num_wrong++;
    }
    return std::to_string(num_wrong) + "/" + std::to_string(len);
}