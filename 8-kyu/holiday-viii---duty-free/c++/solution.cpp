int duty_free(int price, int discount, int holiday_cost)
{
    return holiday_cost / (price * (static_cast<double>(discount) / static_cast<double>(100)));
}