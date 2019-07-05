int F(const int n);
int M(const int n);

int F(const int n) {
    return n == 0 ? 1 : n - M(F(n - 1));
}

int M(const int n) {
    return n == 0 ? 0 : n - F(M(n - 1));
}