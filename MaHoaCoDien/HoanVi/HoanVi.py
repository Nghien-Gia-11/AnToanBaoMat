def matrix(number, key):
    arrTable = []
    for i in range(0, len(key) // number + 1):
        arrTable.append([i])
        for j in range(0, number):
            if len(key) > 7 * i + j:
                arrTable[i].append(key[7 * i + j])
            else:
                arrTable[i].append("x")
    return arrTable


def outputHoanVi(maTrix, arr):
    result = ""
    pos = 0
    for i in range(1, len(arr) + 1):
        if i in arr:
            pos = arr.index(i)
        for j in range(0, len(maTrix)):
            result += str(maTrix[j][pos + 1])
    return result


if __name__ == '__main__':
    numberKey = int(input("nhập số cột : "))
    plaintext = input("nhập plaintext : ")
    print("nhập dãy key : ")
    arrMatrix = list(map(int, input().split(" ")))
    print(matrix(numberKey, plaintext))
    print(outputHoanVi(matrix(numberKey, plaintext), arrMatrix))


# 7
# attackpostponeduntiltwoam
# 4 3 1 2 5 6 7
# TTNAAPTMTSUOAODWCOIXKNLYPETZ
# ttnaaptmtsuoaodwcoixknlxpetx
