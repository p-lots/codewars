class Kata
{
public:
    std::string replaceNth(std::string text, int n, char oldValue, char newValue);
};

std::string Kata::replaceNth(std::string text, int n, char oldValue, char newValue)
{
    if (n < 1) return text;
    std::string::size_type pos = 0;
    int count = 0;
    while ((pos = text.find(oldValue, pos)) != std::string::npos) {
        count++;
        if (count >= n && count % n == 0) {
            text.replace(pos, 1, std::string(1, newValue));
        }
        pos += 1;
    }
    return text;
}