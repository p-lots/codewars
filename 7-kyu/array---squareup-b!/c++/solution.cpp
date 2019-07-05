using namespace std;

vector<int> squareUp(int n)
{
    if (n == 0) return { };
    vector<int> ret;
    for (int max = n + 1; max > 1; max--) {
        for (int i = 1; i <= n; i++) {
            if (i < max) ret.insert(ret.begin(), i);
            else ret.insert(ret.begin(), 0);
        }
    }
    return ret;
}