import math
import Euler


# A^N mod M

def SoNguyenTo(m):
    soNguyenTo = []
    for w in range(2, int(m ** 0.5) + 1):
        while m % w == 0:
            soNguyenTo.append(w)
            m //= w
    if m > 1:
        soNguyenTo.append(m)
    return soNguyenTo


def tinhM(x, y):
    cnt = []
    for j in range(len(x)):
        cnt.append(int(y / x[j]))
    return cnt


def moduloNghichDao(q, b):
    modulo = 0
    for e in range(b):
        if (q * e) % b == 1:
            modulo = e
    return modulo


def dsNghichDao(dsM, listmI):
    lsModulo = []
    for j in range(len(listmI)):
        lsModulo.append(moduloNghichDao(dsM[j], listmI[j]))
    return lsModulo


def dsC(lsModulo, dsM, listmI):
    listC = []
    for j in range(0, len(listmI)):
        listC.append(lsModulo[j] * dsM[j])
    return listC


def dsA(inputA, inputK, listmI):
    listA = []
    for j in range(0, len(listmI)):
        listA.append(Euler.printEuler(inputA, inputK, listmI[j]))
    return listA


def tinhA(lsA, lsC):
    answer = 0
    for i in range(0, len(M)):
        answer += lsA[i] * lsC[i]
    return answer


def phanduTrungHoa(inputK, inputN, inputA):
    dsM = SoNguyenTo(n)
    C = dsC(dsNghichDao(tinhM(dsM, inputN), dsM), tinhM(dsM, inputN), dsM)
    A = dsA(inputA, inputK, dsM)
    phanDuTrungHoa = tinhA(A, C) % n
    return phanDuTrungHoa


if __name__ == '__main__':
    a = int(input("nhập a : "))
    k = int(input("nhập k : "))
    n = int(input("nhập n : "))
    M = SoNguyenTo(n)
    # ds = tinhM(M, n)
    # dsModulo = dsNghichDao(tinhM(M, n), M)
    print(phanduTrungHoa(k, n, a))
