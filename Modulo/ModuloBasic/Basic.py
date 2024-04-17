from Modulo.PhanDuTrungHoa import Euler
from Modulo.Euclid import Euclid


def tinhA1(a, b, x, y, n):
    modAx = Euler.printEuler(a, x, n)
    modBy = Euler.printEuler(b, y, n)
    a1 = (modAx + modBy) % n
    return a1


def tinhA2(a, b, x, y, n):
    modAx = Euler.printEuler(a, x, n)
    modBy = Euler.printEuler(b, y, n)
    if modAx > modBy:
        a2 = (modAx - modBy) % n
    else:
        a2 = (modBy - modAx) % n
    return a2


def tinhA3(a, b, x, y, n):
    modAx = Euler.printEuler(a, x, n)
    modBy = Euler.printEuler(b, y, n)
    a3 = (modAx * modBy) % n
    return a3


def tinhA4(b, y, n):
    modBy = Euler.printEuler(b, y, n)
    a4 = Euclid.modAndThuong(modBy, n)
    return a4


def tinhA5(a, b, x, y, n):
    modAx = Euler.printEuler(a, x, n)
    modBy1 = tinhA4(b, y, n)
    a5 = (modAx * modBy1) % n
    return a5


if __name__ == '__main__':
    inputA = int(input("nhập a : "))
    inputB = int(input("nhập b : "))
    inputX = int(input("nhập x : "))
    inputY = int(input("nhập y : "))
    inputN = int(input("nhập n : "))
    print("A1 : ", tinhA1(inputA, inputB, inputX, inputY, inputN))
    print("A2 : ", tinhA2(inputA, inputB, inputX, inputY, inputN))
    print("A3 : ", tinhA3(inputA, inputB, inputX, inputY, inputN))
    print("A4 : ", tinhA4(inputB, inputY, inputN))
    print("A5 : ", tinhA5(inputA, inputB, inputX, inputY, inputN))
