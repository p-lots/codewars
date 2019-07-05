int growingPlant(int upSpeed, int downSpeed, int desiredHeight)
{
    int height = upSpeed, ret = 1;
    while (height < desiredHeight) {
        height += upSpeed;
        ret++;
        height -= downSpeed;
    }
    return ret;
}