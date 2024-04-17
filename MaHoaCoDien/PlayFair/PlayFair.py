def layKey(inputA, inputM):
    for j in inputM:
        inputA = inputA.replace(j, "")
    arrStr = inputA
    return arrStr


def checkKey(inputM, inputA):
    K = ""
    for i in range(0, len(inputM)):
        if inputM[i] not in K:
            K += inputM[i]
    strMatrix = K + layKey(inputA, K)
    return strMatrix


# ma trận Key
def matrixKey(Str):
    arrTable = []
    for i in range(0, 5):
        arrTable.append([])
    for j in range(0, 5):
        for k in range(0, 5):
            arrTable[j].append(Str[5 * j + k])
    return arrTable


# dãy mã hõa được tách ra
def arrInput(plain):
    result = ""
    cnt = 0
    while cnt < len(plain):
        if cnt + 1 == len(plain):
            result += plain[cnt] + "x" + " "
            break
        if plain[cnt] != plain[cnt + 1]:
            if (cnt + 1) <= len(plain):
                result += plain[cnt] + plain[cnt + 1] + " "
                cnt += 2
        else:
            result += plain[cnt] + "x" + " "
            cnt += 1
    return result.upper()


# ma trận chỉ số được tách ra
def matrixIndex(inputM, inputA, plain):
    matrix = matrixKey(checkKey(inputM, inputA))
    arrKey = arrInput(plain).split()
    matrixPos = []
    check = 0
    for i in range(0, len(arrKey)):
        matrixPos.append([])
    while check < len(arrKey):
        for j in range(0, 2):
            for i in range(0, len(matrix)):
                if arrKey[check][j] in matrix[i]:
                    matrixPos[check].append([i, matrix[i].index(arrKey[check][j])])
        check += 1
    return matrixPos


def outputPlayFair(inputM, inputA, plain):
    result = ""
    matrixPos = matrixIndex(inputM, inputA, plain)
    matrix = matrixKey(checkKey(inputM, inputA))
    for i in range(0, len(matrixPos)):
        if matrixPos[i][0][0] == matrixPos[i][1][0]:
            if matrixPos[i][1][1] == (len(matrix) - 1):
                result += matrix[matrixPos[i][0][0]][matrixPos[i][0][1] + 1]
                result += matrix[matrixPos[i][0][0]][0]
            else:
                result += matrix[matrixPos[i][0][0]][matrixPos[i][0][1] + 1]
                result += matrix[matrixPos[i][0][0]][matrixPos[i][1][1] + 1]
        elif matrixPos[i][0][1] == matrixPos[i][1][1]:
            if matrixPos[i][1][0] == (len(matrix) - 1):
                result += matrix[matrixPos[i][0][0] + 1][matrixPos[i][0][1]]
                result += matrix[0][matrixPos[i][0][1]]
            else:
                result += matrix[matrixPos[i][0][0] + 1][matrixPos[0][0][1]]
                result += matrix[matrixPos[i][1][0] + 1][matrixPos[0][1][1]]
        else:
            result += matrix[matrixPos[i][0][0]][matrixPos[i][1][1]]
            result += matrix[matrixPos[i][1][0]][matrixPos[i][0][1]]
    return result


if __name__ == '__main__':
    A = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    M = "MONARCHY"
    M = M.upper()
    plaintext = input("nhập plaintext : ")
    print(outputPlayFair(M, A, plaintext))
