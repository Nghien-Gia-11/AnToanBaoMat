
def Shift(L, R, i):
    arrRound = [1, 2, 9, 16]
    resultL = ""
    resultR = ""
    if i in arrRound:
        for i in range(2, len(L) + 1):
            resultL += L[i-1]
            resultR += R[i-1]
        resultL += L[0]
        resultR += R[0]
    else:
        for i in range(3, len(L) + 1):
            resultL += L[i-1]
            resultR += R[i-1]
        resultL += L[0]
        resultR += R[0]
        resultL += L[1]
        resultR += R[1]
    return resultL, resultR


if __name__ == '__main__':
    inputL = input("nhập L : ")
    inputR = input("nhập R : ")
    roundShift = int(input("nhập vòng dịch : "))
    Shift(inputL, inputR, roundShift)


