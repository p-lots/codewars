std::vector<std::vector<int>> rotateMatrixLeft(std::vector<std::vector<int>> matrix)
{
    unsigned height_orig = matrix.size(), width_orig = matrix.front().size();
    unsigned height_new = width_orig, width_new = height_orig;
    std::vector<std::vector<int>> ret(height_new, std::vector<int>(width_new, 0));
    int k = width_orig - 1;
    for (unsigned i = 0; i < height_new; i++) {
        int l = 0;
        for (unsigned j = 0; j < width_new; j++) {
            ret[i][j] = matrix[l][k];
            l++;
        }
        k--;
    }
    return ret;
}