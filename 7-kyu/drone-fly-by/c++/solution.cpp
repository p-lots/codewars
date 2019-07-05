std::string flyBy(std::string lamp, std::string drone)
{
    int drone_pos = -1;
    for (unsigned i = 0; i < drone.length(); i++) {
        if (drone[i] == 'T') {
            drone_pos = i;
            break;
        }
    }
    if (drone_pos > -1) {
        for (unsigned i = 0; i <= drone_pos; i++) {
            lamp[i] = 'o';
        }
    }
    return lamp;
}