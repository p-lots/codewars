#include <string>
using namespace std;

string calculateScore(string str)
{
    int left_score = 0, right_score = 0;
    for (const char &c : str) {
        switch (c) {
            case 'w':
            left_score += 4;
            break;
            case 'p':
            left_score += 3;
            break;
            case 'b':
            left_score += 2;
            break;
            case 's':
            left_score += 1;
            break;
            case 'm':
            right_score += 4;
            break;
            case 'q':
            right_score += 3;
            break;
            case 'd':
            right_score += 2;
            break;
            case 'z':
            right_score += 1;
            break;
            default:
            break;
        }
    }
    return left_score > right_score ? "Left side wins!" : left_score == right_score ? "Let's fight again!" : "Right side wins!";
}

string alphabetWar(string fight)
{
    string after_bombs = fight;
    for (unsigned i = 0; i < after_bombs.length(); i++) {
        if (after_bombs.length() > 1 && after_bombs[i] == '*') {
            after_bombs[i] = '_';
            if (i == 0 && after_bombs[i + 1] != '*') after_bombs[i + 1] = '_';
            else if (i == after_bombs.length() - 1 && after_bombs[i - 1] != '*') after_bombs[i - 1] = '_';
            else if (i > 0 && i < after_bombs.length() - 1) {
                after_bombs[i - 1] = after_bombs[i - 1] == '*' ? after_bombs[i - 1] : '_';
                after_bombs[i + 1] = after_bombs[i + 1] == '*' ? after_bombs[i + 1] : '_';
            }
        }
    }
    return calculateScore(after_bombs);
}