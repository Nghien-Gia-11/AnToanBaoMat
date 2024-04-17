import modulo


# A^N mod M


def SoNguyenTo(m):
    soNguyenTo = []
    for w in range(2, int(m ** 0.5) + 1):
        while m % w == 0:
            cnt = 0
            while m % w == 0:
                cnt += 1
                m //= w
            soNguyenTo.append([w, cnt])
    if m > 1:
        soNguyenTo.append([m, 1])
    return soNguyenTo


def compareArr(arrA, arrB):
    arrNguyenTo = []
    for i in range(0, len(arrB)):
        arrNguyenTo.append(arrB[i][0])
    for i in range(0, len(arrA)):
        if arrA[i][0] in arrNguyenTo:
            return False
    return True


def tinhPhiM(b):
    cnt = 1
    for i in range(0, len(b)):
        cnt *= b[i][0] ** b[i][1] - b[i][0] ** (b[i][1] - 1)
    return cnt


def rutGonMu(phiM, muN):
    muRutGon = muN % phiM
    return muRutGon


def printEuler(A, N, M):
    arrNguyenToN = SoNguyenTo(N)
    arrNguyenToM = SoNguyenTo(M)
    if compareArr(arrNguyenToN, arrNguyenToM):
        return modulo.printKetQuaMod(A, rutGonMu(tinhPhiM(arrNguyenToM), N), M)
    else:
        return modulo.printKetQuaMod(A, N, M)


if __name__ == '__main__':
    intputA = int(input())
    intputN = int(input())
    intputM = int(input())
    print(printEuler(intputA, intputN, intputM))
