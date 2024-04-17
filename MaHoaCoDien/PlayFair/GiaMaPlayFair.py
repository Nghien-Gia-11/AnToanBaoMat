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
def arrInput(cipher):
    result = ""
    cnt = 0
    while cnt < len(cipher):
        if cnt + 1 == len(cipher):
            result += cipher[cnt] + "x" + " "
            break
        if cipher[cnt] != cipher[cnt + 1]:
            if (cnt + 1) <= len(cipher):
                result += cipher[cnt] + cipher[cnt + 1] + " "
                cnt += 2
        else:
            result += cipher[cnt] + "x" + " "
            cnt += 1
    return result.upper()


# ma trận chỉ số được tách ra
def matrixIndex(inputM, inputA, cipher):
    matrix = matrixKey(checkKey(inputM, inputA))
    arrKey = arrInput(cipher).split()
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


def outputPlayFair(inputM, inputA, cipher):
    result = ""
    matrixPos = matrixIndex(inputM, inputA, cipher)
    matrix = matrixKey(checkKey(inputM, inputA))
    for i in range(0, len(matrixPos)):
        if matrixPos[i][0][0] == matrixPos[i][1][0]:
            if matrixPos[i][1][1] == 0:
                result += matrix[matrixPos[i][0][0]][matrixPos[i][0][1] - 1]
                result += matrix[matrixPos[i][0][0]][4]
            else:
                result += matrix[matrixPos[i][0][0]][matrixPos[i][0][1] - 1]
                result += matrix[matrixPos[i][0][0]][matrixPos[i][1][1] - 1]
        if matrixPos[i][0][1] == matrixPos[i][1][1]:
            if matrixPos[i][1][0] == 0:
                result += matrix[matrixPos[i][0][0] - 1][matrixPos[i][0][1]]
                result += matrix[4][matrixPos[i][0][1]]
            else:
                result += matrix[matrixPos[i][0][0] - 1][matrixPos[0][0][1]]
                result += matrix[matrixPos[i][1][0] - 1][matrixPos[0][1][1]]
        else:
            result += matrix[matrixPos[i][0][0]][matrixPos[i][1][1]]
            result += matrix[matrixPos[i][1][0]][matrixPos[i][0][1]]
    return result


if __name__ == '__main__':
    A = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    M = "MONARCHY"
    M = M.upper()
    ciphertext = input("nhập ciphertext : ")
    print(matrixIndex(M, A, ciphertext))
    print(outputPlayFair(M, A, ciphertext))
