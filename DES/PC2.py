
def valuePC2(n):
    result = ""
    i = [14, 17, 11, 24, 1, 5, 3, 28,
         15, 6, 21, 10, 23, 19, 12, 4,
         26, 8, 16, 7, 27, 20, 13, 2]
    j = [41, 52, 31, 37, 47, 55, 30, 40,
         51, 45, 33, 48, 44, 49, 39, 56,
         34, 53, 46, 42, 50, 36, 29, 32]
    for t in i:
        result += n[t - 1]
    for t in j:
        result += n[t - 1]
    return result


if __name__ == '__main__':
    inputPC2 = input()
    valuePC2(inputPC2)
