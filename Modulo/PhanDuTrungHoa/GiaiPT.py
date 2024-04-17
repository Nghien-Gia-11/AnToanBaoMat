from Modulo.Euclid import Euclid


def lsModM(M, Mi):
    lsMod = []
    for i in range(0, len(M)):
        lsMod.append(Euclid.modAndThuong(M[i], Mi[i]))
    return lsMod


def GiaiPT(lsM, lsA, lsMi, _M):
    arrMod = lsModM(arrM, lsMi)
    cnt = 0
    for i in range(0, len(arrMod)):
        cnt += lsM[i] * lsA[i] * arrMod[i]

    result = cnt % _M
    return result


if __name__ == '__main__':
    m1 = int(input("nhập m1 : "))
    m2 = int(input("nhập m2 : "))
    m3 = int(input("nhập m3 : "))
    a1 = int(input("nhập a1 : "))
    a2 = int(input("nhập a2 : "))
    a3 = int(input("nhập a3 : "))
    M = m1 * m2 * m3
    arrM = [m2 * m3, m1 * m3, m1 * m2]
    arrA = [a1, a2, a3]
    arrMi = [m1, m2, m3]
    print(arrA)
    print(lsModM(arrM, arrMi))
    print(arrM)
    print(GiaiPT(arrM, arrA, arrMi, M))

