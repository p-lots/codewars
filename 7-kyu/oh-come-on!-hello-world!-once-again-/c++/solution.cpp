std::string f() 
{
    std::string s = "xxxxxxxxxxxxx";
    s[0] -= 48;
    s[1] -= 19;
    s[2] -= 12;
    s[3] = s[2];
    s[4] -= 9;
    s[5] -= 76;
    s[6] -= 88;
    s[7] -= 1;
    s[8] = s[4];
    s[9] -= 6;
    s[10] = s[2];
    s[11] -= 20;
    s[12] -= 87;
    return s;
}