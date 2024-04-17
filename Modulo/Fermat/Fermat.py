import math


def checkNguyenTo(N):
    check = True
    for i in range(2, N//2 + 1):
        if N % i == 0:
            check = False
    return check


def checkModP(A, N):
    if A % N == 0:
        return False
    else:
        return True


def modM(M, modMu):
    return M % modMu


def Fermat(A, M, N):
    if not checkNguyenTo(N) | checkModP(A, N):
        return "không sử dụng được định lý Fermat"
    else:
        mu = N - 1
        result = (A ** modM(M, mu)) % N
        return result


if __name__ == '__main__':
    inputA = int(input("nhập a : "))
    inputM = int(input("nhập M : "))
    inputN = int(input("nhập N : "))
    print(Fermat(inputA, inputM, inputN))
