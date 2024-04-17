import math


# đoạn code này để tính modulo # A^N mod M


# tính modulo của a^i mod m
def modAiModM(a, x, m):
    modNhiPhan = [a]
    for i in range(1, x + 1):
        y = (modNhiPhan[i - 1] ** 2) % m
        modNhiPhan.append(y)
    return modNhiPhan


# lấy các số mũ tổng = n
def soMuTongN(x, n):
    arrTongMuN = []
    t = n
    for i in range(x, -1, -1):
        if t >= 2 ** i:
            t = t - 2 ** i
            arrTongMuN.append(i)
        if t <= 2 ** (i - 1):
            i -= 1
    return arrTongMuN


# lấy ra các số dư của a^n mod m
def ketQuaMod(arrTongMuN, modNhiPhan, m):
    arrModM = []
    for i in arrTongMuN:
        arrModM.append(modNhiPhan[i])
    s = 1
    for i in arrModM:
        s *= i
    mod = s % m
    return mod


def printKetQuaMod(intputA, intputN, intputM):
    if intputN == 0:
        XNhiPhan = 1
    else:
        XNhiPhan = int(math.log2(intputN))
    modAiModM(intputA, XNhiPhan, intputM)
    soMuTongN(XNhiPhan, intputN)
    return ketQuaMod(soMuTongN(XNhiPhan, intputN), modAiModM(intputA, XNhiPhan, intputM), intputM)


if __name__ == '__main__':
    A = int(input())
    N = int(input())
    M = int(input())
    print(printKetQuaMod(A, N, M))
