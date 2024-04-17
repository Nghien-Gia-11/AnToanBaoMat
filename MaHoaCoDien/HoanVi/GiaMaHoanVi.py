def divStr(strSBox, key):
    cnt = 0
    lsStrSbox = list(strSBox)
    while cnt <= len(strSBox)+3:
        cnt += (len(strSBox) // key)
        lsStrSbox.insert(cnt, " ")
        cnt += 1
    result = ""
    for i in range(0, len(lsStrSbox)):
        result += lsStrSbox[i]
    return result


def outputGiaiMa(plain, key, arr):
    result = ""
    matrix = divStr(plain, key).split()
    for j in range(0, (len(plain) // key)):
        for i in arr:
            result += matrix[i-1][j]
    return result


if __name__ == '__main__':
    numberKey = int(input("nhập số cột : "))
    plaintext = input("nhập plaintext : ")
    print(len(plaintext))
    print("nhập dãy key : ")
    arrMatrix = list(map(int, input().split(" ")))
    print(outputGiaiMa(plaintext, numberKey, arrMatrix))

# 7
# attackpostponeduntiltwoam
# 4 3 1 2 5 6 7
# TTNA APTM TSUO AODW COIX KNLY PETZ
# TTNAAPTMTSUOAODWCOIXKNLYPETZ
# ttnaaptmtsuoaodwcoixknlxpetx
