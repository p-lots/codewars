#include <cmath>

class Movie
{
public:
    static int movie(int card, int ticket, double perc);
};

int Movie::movie(int card, int ticket, double perc)
{
    int ret = 1;
    double card_price = static_cast<double>(card) + static_cast<double>(ticket) * perc;
    int total_ticket = ticket;
    while (!(std::ceil(card_price) < total_ticket)) {
        card_price += static_cast<double>(ticket) * std::pow(perc, ++ret);
        total_ticket += ticket;
    }
    return ret;
}