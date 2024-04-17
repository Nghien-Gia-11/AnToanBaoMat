
def convertBIN(cnt):
    strIP = ""
    for x in range(0, 4):
        if cnt % 2 == 0:
            strIP += "0"
        else:
            strIP += "1"
        cnt = cnt // 2
    return strIP[::-1]


def valueBIN(inputStr):
    cnt = ""
    for i in range(0, len(inputStr)):
        if inputStr[i].__contains__("A"):
            cnt += convertBIN(10)
        elif inputStr[i].__contains__("B"):
            cnt += convertBIN(11)
        elif inputStr[i].__contains__("C"):
            cnt += convertBIN(12)
        elif inputStr[i].__contains__("D"):
            cnt += convertBIN(13)
        elif inputStr[i].__contains__("E"):
            cnt += convertBIN(14)
        elif inputStr[i].__contains__("F"):
            cnt += convertBIN(15)
        else:
            cnt += convertBIN(int(inputStr[i]))
    return cnt


if __name__ == '__main__':
    Str = input("nhập dãy : ")
    print(valueBIN(Str))
    print()
# 0F1571C947D9E859
# 0000111100010101011100011100100101000111110110011110100001011001
