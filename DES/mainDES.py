from DES import convertBIN, convertHEX, E, IP, IP1, LeftShift, P, PC1, PC2, SBox, Swap, XOR_EK, XOR_LP


def valuePC1(key):
    keyBIN = convertBIN.valueBIN(key)
    value = PC1.PC1(keyBIN)
    return value


def valueIP(plainText):
    plainBIN = convertBIN.valueBIN(plainText)
    value = IP.ValueIP(plainBIN)
    return value


if __name__ == '__main__':
    inputKey = input("nhập key : ").upper()
    inputPlainText = input("nhập PlainText : ").upper()
    keyL0 = valuePC1(inputKey)[0]
    keyR0 = valuePC1(inputKey)[1]

    # tìm danh sách key
    desKey = []
    for i in range(1, 17):
        # print("vòng ", format(i))
        keyL0 = LeftShift.Shift(keyL0, keyR0, i)[0]
        keyR0 = LeftShift.Shift(keyL0, keyR0, i)[1]
        desKey.append(PC2.valuePC2(keyL0 + keyR0))
    bin2 = convertHEX.valueHEX(desKey[1])
    print(bin2)
    plainL0 = valueIP(inputPlainText)[0]
    plainR0 = valueIP(inputPlainText)[1]
    print(plainL0)
    print(plainR0)
    for i in range(1, 17):
        e = E.ERi(plainR0)
        print("e : ", e)
        xor = XOR_EK.XOR_EK(e, desKey[i - 1])
        print("key : ", desKey[i-1])
        print("xor : ", xor)
        box = SBox.valueSBox(xor)
        print("sbox : ", box)
        p = P.valueP(box)
        print("P : ", p)
        tem = plainR0
        plainR0 = XOR_LP.valueXOR_LP(plainL0, p)
        print("R : ", plainR0)
        plainL0 = tem
        print("L : ", plainL0)
        print()
    swap = Swap.swapFinish(plainL0, plainR0)
    result = IP1.valueIP1(swap)
    print(result)
    answer = convertHEX.valueHEX(result)
    print(answer)
# key : 0f1571c947d9e859   F35D514714F45A8A
# plain : 02468aceeca86420    1EDE3CBCAF288822
# cipher : da02ce3a89ecac3b
# CC88A7530A4981A9
# CC88A7530A4981A9
