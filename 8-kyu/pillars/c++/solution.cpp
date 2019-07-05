long pillars(int num_of_pillars, int distance, int width)
{
    if (num_of_pillars < 2) return 0;
    return distance * 100 * (num_of_pillars - 1) + width * (num_of_pillars - 2);
}