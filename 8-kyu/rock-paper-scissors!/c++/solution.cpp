#include <string>

std::string rps(const std::string& p1, const std::string& p2)
{
    if (p1.front() == p2.front()) return "Draw!";
    if (p1.front() == 's') {
        if (p2.front() == 'p') return "Player 1 won!";
        else if (p2.front() == 'r') return "Player 2 won!";
    }
    if (p1.front() == 'r') {
        if (p2.front() == 'p') return "Player 2 won!";
        else if (p2.front() == 's') return "Player 1 won!";
    }
    if (p1.front() == 'p') {
        if (p2.front() == 's') return "Player 2 won!";
        else if (p2.front() == 'r') return "Player 1 won!";
    }
}