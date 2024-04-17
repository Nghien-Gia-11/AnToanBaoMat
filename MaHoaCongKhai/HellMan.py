from Modulo.PhanDuTrungHoa import modulo


def checkNguyenTo(N):
    check = True
    for j in range(2, N//2 + 1):
        if N % j == 0:
            check = False
    return check


def HellMan(q, a, xA, xB):
    yA = modulo.printKetQuaMod(a, xA, q)
    yB = modulo.printKetQuaMod(a, xB, q)
    K = modulo.printKetQuaMod(yA, xB, q)
    return yA, yB, K


if __name__ == '__main__':
    inputQ = int(input("nhập q : "))
    inputa = int(input("nhập a : "))
    inputXa = int(input("nhập xA : "))
    inputXb = int(input("nhập xB : "))
    for i in range(0, 3):
        print(HellMan(inputQ, inputa, inputXa, inputXb)[i])
