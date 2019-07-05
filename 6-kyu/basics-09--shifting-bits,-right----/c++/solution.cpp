int nextLower(int n)
{
	  int m;
    if (n > 0) {
        m = 0x01;
        while (m < n) m <<= 1;
        m >>= 1;
    }
    else if (n < 0) {
        m = -0x01;
        while (m >= n) m <<= 1;
    }
    else return -1;
    return m;
}