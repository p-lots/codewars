#include <utility>
#include <vector>

bool chessBoardCellColor(std::string cell1, std::string cell2) {
    const std::vector<std::vector<bool> > board = {
        { true, false, true, false, true, false, true, false },
        { false, true, false, true, false, true, false, true },
        { true, false, true, false, true, false, true, false },
        { false, true, false, true, false, true, false, true },
        { true, false, true, false, true, false, true, false },
        { false, true, false, true, false, true, false, true },
        { true, false, true, false, true, false, true, false },
        { false, true, false, true, false, true, false, true }
    };
    auto c1 = std::make_pair(cell1[0] - 'A', cell1[1] - '1');
    auto c2 = std::make_pair(cell2[0] - 'A', cell2[1] - '1');
    return board[c1.first][c1.second] == board[c2.first][c2.second];
}