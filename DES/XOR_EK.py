
def XOR_EK(E, K):
    result = ""
    for i in range(0, 48):
        if E[i] == K[i]:
            result += "0"
        else:
            result += "1"
    return result


if __name__ == '__main__':
    inputE = input("nhập E : ")
    inputK = input("nhập K : ")
    XOR_EK(inputE, inputK)
    # print(XOR_EK(inputE, inputK))
