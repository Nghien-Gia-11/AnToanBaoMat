from MaHoaCongKhai import HellMan
from Modulo.Logarit import CanNguyenThuy
from Modulo.PhanDuTrungHoa import Euler
from Modulo.Euclid import Euclid


def checkNguyenTo(Q):
    if not HellMan.checkNguyenTo(Q):
        return False
    else:
        return True


def checkCanNguyenThuy(A, Q):
    if not CanNguyenThuy.checkCanNguyenThuy(A, Q):
        return False
    else:
        return True


def tinhYa(A, xA, q):
    yA = Euler.printEuler(A, xA, q)
    return yA


def banMaC(A, xA, q, k, M):
    yA = tinhYa(A, xA, q)
    K = Euler.printEuler(yA, k, q)
    C1 = Euler.printEuler(A, k, q)
    C2 = (M * K) % q
    return C1, C2, K


def giaiMaC(C1, C2, xA, q):
    K = Euler.printEuler(C1, xA, q)
    x = Euclid.modAndThuong(K, q)
    M = (x * C2) % q
    return M


if __name__ == '__main__':
    inputQ = int(input("nhập q : "))
    inputA = int(input("nhập a : "))
    inputXa = int(input("nhập xA : "))
    inputK = int(input("nhập k : "))
    inputM = int(input("nhập m : "))
    print(tinhYa(inputA, inputXa, inputQ))
    c1 = banMaC(inputA, inputXa, inputQ, inputK, inputM)[0]
    c2 = banMaC(inputA, inputXa, inputQ, inputK, inputM)[1]
    key = c2 = banMaC(inputA, inputXa, inputQ, inputK, inputM)[2]
    print("PU : { ", inputQ, ", ", inputA, ", ", tinhYa(inputA, inputXa, inputQ), "}")
    print("(C1, C2) : (", c1, ", ", c2, " )")
    print("giải mã (C1, C2) : ", giaiMaC(c1, c2, inputXa, inputQ))
    print(key)
# 7433 3 341 872 403
