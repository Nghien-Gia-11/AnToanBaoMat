from Modulo.PhanDuTrungHoa import Euler


def tinhN(q, p):
    return q * p


def phiN(q, p):
    return (q - 1)*(p - 1)


def tinhD(q, p, e):
    d = 0
    for i in range(0, phiN(q, p)):
        if (i * e) % phiN(q, p) == 1:
            d = i
    return d


# C = M ^ d
def AnMaHoa(q, p, e, M):
    d = tinhD(q, p, e)
    n = tinhN(q, p)
    C = Euler.printEuler(M, d, n)
    return C


def BaGiaiMa(q, p, e, C):
    n = tinhN(q, p)
    result = Euler.printEuler(C, e, n)
    return result


def BaMaHoa(q, p, e, M):
    n = tinhN(q, p)
    C = Euler.printEuler(M, e, n)
    return C


def AnGiaiMa(q, p, e, C):
    n = tinhN(q, p)
    d = tinhD(q, p, e)
    result = Euler.printEuler(C, d, n)
    return result


if __name__ == '__main__':
    inputP = int(input("nhập p : "))
    inputQ = int(input("nhập q : "))
    inputE = int(input("nhập e : "))
    inputM = int(input("nhập m : "))
    inputC = int(input("nhập c : "))
    print(tinhN(inputQ, inputP))
    print(tinhD(inputP, inputQ, inputE))
    # print(AnMaHoa(inputQ, inputP, inputE, inputM))  67
    # print(BaGiaiMa(inputQ, inputP, inputE, inputC))  1479
    # print(BaMaHoa(inputQ, inputP, inputE, inputM))  67
    # print(AnGiaiMa(inputQ, inputP, inputE, inputC))  1906
