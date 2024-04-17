import math
from Modulo.PhanDuTrungHoa import Euler


def tinhPhiN(N):
    lsNguyenTo = Euler.SoNguyenTo(N)
    phiN = Euler.tinhPhiM(lsNguyenTo)
    return phiN


def dsUocPhiN(phiN):
    cntUocPhiN = []
    for j in range(2, int(phiN / 2) + 1):
        if phiN % j == 0:
            cntUocPhiN.append(j)
    cntUocPhiN.append(phiN)
    return cntUocPhiN


# danh sách mod của A mũ ước của phi N
def dsMod(A, N, listsUocPhi):
    listMod = []
    for i in listsUocPhi:
        listMod.append(Euler.printEuler(A, i, N))
    return listMod


def checkCanNguyenThuy(A, N):
    lsUocPhi = dsUocPhiN(tinhPhiN(N))
    listMod = dsMod(A, N, lsUocPhi)
    t = 0
    check = True
    while t != len(listMod) - 1:
        if listMod[t] == 1:
            check = False
        t += 1
    return check


if __name__ == '__main__':
    inputA = int(input("nhập A : "))
    inputN = int(input("nhập N : "))
    if checkCanNguyenThuy(inputA, inputN):
        print("a là căn nguyên thủy của n")
    else:
        print("a không là ăn nguyên thủy của n")
