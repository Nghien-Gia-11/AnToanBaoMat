from Modulo.PhanDuTrungHoa import Euler
from Modulo.Euclid import Euclid


def tinhYa(h, p, q, xA):
    g = Euler.printEuler(h, (p-1)/q, p)
    yA = Euler.printEuler(g, xA, p)
    return g, yA


def tinhRS(h, p, q, xA, HM, k):
    g = tinhYa(h, p, q, xA)[0]
    gK = Euler.printEuler(g, k, p)
    r = gK % q
    k1 = Euclid.modAndThuong(k, q)
    modHMXR = (HM + xA * r) % q
    s = (k1 * modHMXR) % q
    return r, s


def comfirm(HM, r, s, q, p, h, xA):
    w = Euclid.modAndThuong(s, q)
    u1 = (HM * w) % q
    u2 = (r * w) % q
    g = tinhYa(h, p, q, xA)[0]
    yA = tinhYa(h, p, q, xA)[1]
    modGu1 = Euler.printEuler(g, u1, p)
    modYu2 = Euler.printEuler(yA, u2, p)
    modGY = (modGu1 * modYu2) % p
    v = modGY % q
    if v == r:
        return True
    else:
        return False


if __name__ == '__main__':
    inputHM = int(input("nhập H(M) : "))
    inputP = int(input("nhập p : "))
    inputQ = int(input("nhập q : "))
    inputH = int(input("nhập h : "))
    inputXa = int(input("nhập xA : "))
    inputK = int(input("nhập k : "))
    R = tinhRS(inputH, inputP, inputQ, inputXa, inputHM, inputK)[0]
    S = tinhRS(inputH, inputP, inputQ, inputXa, inputHM, inputK)[1]
    print(tinhYa(inputH, inputP, inputQ, inputXa)[1])
    print(R, S)
    if comfirm(inputHM, R, S, inputQ, inputP, inputH, inputXa):
        print("chữ ký đúng !!")
    else:
        print("chữ ký sai !!")

# HM = 7 p = 89 q = 11 h = 38 xA = 5 k = 2
