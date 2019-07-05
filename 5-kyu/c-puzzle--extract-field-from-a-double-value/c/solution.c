typedef struct {
    unsigned long long mantissa : 52;
    unsigned long long exponent : 11;
    unsigned long long sign : 1;
} dbl;

typedef union {
    dbl first;
    double second;
} dbl_u;

int exponent(double d)
{
 dbl_u d_u;
 d_u.second = d;
 return d_u.first.exponent;
}