class Kata
{
public:
    std::vector<std::string> towerBuilder(int nFloors)
    {
        std::vector<std::string> ret;
        for (int i = 0, spaces = nFloors - 1, stars = 1; i < nFloors; i++) {
            std::string line = "";
            if (spaces > 0) line += std::string(spaces, ' ');
            line += std::string(stars, '*');
            if (spaces > 0) line += std::string (spaces, ' ');
            ret.push_back(line);
            spaces--;
            stars += 2;
        }
        return ret;
    }
};