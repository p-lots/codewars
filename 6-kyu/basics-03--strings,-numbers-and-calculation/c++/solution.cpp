#include <cctype>
#include <cmath>
#include <string>

int do_operation(std::string n1, std::string n2, char op)
{
    double n1_d = std::stod(n1), n2_d = std::stod(n2);
    int result = 0;
    switch (op) {
        case '+':
        result = std::round(n1_d + n2_d);
        break;
        case '-':
        result = std::round(n1_d - n2_d);
        break;
        case '*':
        result = std::round(n1_d * n2_d);
        break;
        case '/':
        result = std::round(n1_d / n2_d);
        break;
        default:
        break;
    }
    return result;
}

std::string calculateString(std::string calcIt) 
{
    std::string result = "", n1 = "", n2 = "";
    char op;
    bool found_op = false;
    for (unsigned i = 0; i < calcIt.length(); i++) {
        if ((std::isdigit(calcIt[i]) || calcIt[i] == '.') && !found_op) {
            n1 += calcIt[i];
        }
        else if (std::isdigit(calcIt[i]) || calcIt[i] == '.') {
            n2 += calcIt[i];
        }
        else if (calcIt[i] == '+' || calcIt[i] == '-'
            || calcIt[i] == '*' || calcIt[i] == '/') {
            found_op = true;
            op = calcIt[i];
        }
    }
    result = std::to_string(do_operation(n1, n2, op));
    return result;
}   