long pillars(int num_of_pillars, int distance, int width)
{
    if (num_of_pillars < 2) return 0;
    int counted_pillars = num_of_pillars - 2;
    return distance * 100 * (counted_pillars + 1) + width * counted_pillars;
}

// |_|----|_|----|_|----|_|----|_|