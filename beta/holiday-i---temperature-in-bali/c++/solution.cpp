bool bareable(int heat, double humidity) {
    if (heat > 35 || humidity > 0.5) return false;
    else if (heat > 25 && humidity > 0.4) return false;
    return true;
}