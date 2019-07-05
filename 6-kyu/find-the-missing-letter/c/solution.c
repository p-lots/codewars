char findMissingLetter(char array[], int arrayLength)
{
    char ret = ' ';
    for (unsigned i = 1; i < arrayLength; i++) {
        if (array[i] != array[i - 1] + 1) {
            ret = array[i - 1] + 1;
        }
    }
    return ret;
}