
def ERi(n):
    i = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17]
    j = [16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]
    E = ""
    for t in i:
        E += n[t - 1]
    for t in j:
        E += n[t - 1]
    return E


if __name__ == '__main__':
    plainText = input("nhập plaintext : ")
    ERi(plainText)
    print(ERi(plainText))
