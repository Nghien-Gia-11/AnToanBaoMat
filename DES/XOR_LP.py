
def valueXOR_LP(L, P):
    result = ""
    for i in range(0, 32):
        if P[i] == L[i]:
            result += "0"
        else:
            result += "1"
    return result


if __name__ == '__main__':
    inputL = input("nhập L :")
    inputP = input("nhập P :")
    valueXOR_LP(inputL, inputP)
