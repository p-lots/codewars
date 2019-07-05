std::vector<int> L(int n, int L0, int L1, int add)
{
    std::vector<int> ret = { L0, L1 };
    for (unsigned i = 2; i < n; i++) {
        ret.push_back(ret[i - 1] + ret[i - 2] + add);
    }
    return ret;
}