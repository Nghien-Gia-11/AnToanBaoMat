from DES import SBox


def divStr(strSBox):
    result = ""
    for i in range(0, len(strSBox), 4):
        result += strSBox[i:i+4] + " "
    return result


def convertDEC(strSBox):
    dsDEC = divStr(strSBox)
    dsDEC = dsDEC.split()
    result = ""
    for i in range(0, len(dsDEC)):
        result += str(int(dsDEC[i][0]) * 2 ** 3 + int(dsDEC[i][1]) * 2 ** 2 + int(dsDEC[i][2]) * 2 ** 1 + int(dsDEC[i][3]) * 2 ** 0) + " "
    return result


def valueHEX(inputStr):
    lsDEC = convertDEC(inputStr).split(" ")
    cnt = ""
    for i in range(0, len(lsDEC)):
        if lsDEC[i].__contains__("10"):
            cnt += "A"
        elif lsDEC[i].__contains__("11"):
            cnt += "B"
        elif lsDEC[i].__contains__("12"):
            cnt += "C"
        elif lsDEC[i].__contains__("13"):
            cnt += "D"
        elif lsDEC[i].__contains__("14"):
            cnt += "E"
        elif lsDEC[i].__contains__("15"):
            cnt += "F"
        else:
            cnt += lsDEC[i]
    return cnt


if __name__ == '__main__':
    Str = input("nhập dãy : ")
    print(valueHEX(Str))
    print(divStr(Str))
# 0F1571C947D9E859
# 0000111100010101011100011100100101000111110110011110100001011001
