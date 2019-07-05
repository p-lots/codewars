std::string cake(int x, std::string y)
{
    int total = 0;
    for (unsigned i = 0; i < y.length(); i++) {
        if (i % 2 == 0) total += static_cast<int>(y[i]);
        else total += static_cast<int>(y[i]) - 96;
    }
    auto result = static_cast<double>(total) / static_cast<double>(x);
    return result > 0.7 ? "Fire!" : "That was close!";
}