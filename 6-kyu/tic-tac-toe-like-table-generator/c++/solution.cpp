#include <numeric>
#include <string>
#include <sstream>
#include <vector>

std::string displayBoard(const std::vector<char>& board, unsigned short width)
{
    std::stringstream ret;
    unsigned rows = board.size() / width;
    for (unsigned short i = 0; i < rows; i++) {
        for (unsigned short j = 0; j < width; j++) {
            ret << " " << board.at(i * width + j) << " ";
            if (j < width - 1) ret << "|";
        }
        if (i < rows - 1) ret << '\n' << std::string(width * 3 + width - 1, '-') << '\n';
    }
    return ret.str();
}