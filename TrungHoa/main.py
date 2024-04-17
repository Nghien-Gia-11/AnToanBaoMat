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


if __name__ == '__main__':
    a = int(input("nhập a : "))
    k = int(input("nhập k : "))
    n = int(input("nhập n : "))
    M = SoNguyenTo(n)
    print(M)
    ds = tinhM(M, n)
    print(ds)
    dsModulo = []
    for i in range(len(M)):
        dsModulo.append(moduloNghichDao(ds[i], M[i]))
    print(dsModulo)
    C = []
    for i in range(0, len(M)):
        C.append(dsModulo[i] * ds[i])
    print(C)
    A = []
    for i in range(0, len(M)):
        A.append(Euler.printEuler(a, k, M[i]))
    print(A)

    answer = 0
    for i in range(0, len(M)):
        answer += A[i] * C[i]

    phanDuTrungHoa = answer % n
    print(phanDuTrungHoa)
