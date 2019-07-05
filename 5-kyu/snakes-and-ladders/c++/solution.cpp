#include <map>
#include <string>

class SnakesLadders
{
    public:
        SnakesLadders()
        {
            p1_pos = 0;
            p2_pos = 0;
            game_over = false;
            p1_turn = true;
        };
        std::string play(int die1, int die2);
    private:
        const std::map<int, int> move_map = {
            {  2, 38 }, {  7, 14 }, {  8, 31 }, { 15, 26 },
            { 16,  6 }, { 21, 42 }, { 28, 84 }, { 36, 44 },
            { 46, 25 }, { 49, 11 }, { 51, 67 }, { 62, 19 },
            { 64, 60 }, { 71, 91 }, { 74, 53 }, { 78, 98 },
            { 87, 94 }, { 89, 68 }, { 92, 88 }, { 95, 75 },
            { 99, 80 }
        };
        int p1_pos;
        int p2_pos;
        bool game_over;
        bool p1_turn;
};

std::string SnakesLadders::play(int die1, int die2)
{
    if (p1_turn) {
        p1_pos += die1 + die2;
        if (p1_pos > 100) p1_pos = 200 - p1_pos;
        if (move_map.count(p1_pos) == 1) p1_pos = move_map.at(p1_pos);
    }
    else {
        p2_pos += die1 + die2;
        if (p2_pos > 100) p2_pos = 200 - p2_pos;
        if (move_map.count(p2_pos) == 1) p2_pos = move_map.at(p2_pos);
    }
    if (game_over) return "Game over!";
    else if (p1_pos == 100) {
        game_over = true;
        return "Player 1 Wins!";
    }
    else if (p2_pos == 100) {
        game_over = true;
        return "Player 2 Wins!";
    }
    if (p1_turn) {
        if (die1 != die2) p1_turn = !(p1_turn);
        return "Player 1 is on square " + std::to_string(p1_pos);
    }
    else {
        if (die1 != die2) p1_turn = !(p1_turn);
        return "Player 2 is on square " + std::to_string(p2_pos);
    }
}