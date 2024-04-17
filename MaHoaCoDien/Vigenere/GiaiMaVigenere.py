from MaHoaCoDien.Ceaser import Ceaser


def lapKey(inputC, inputK):
    Key = ""
    if len(inputK) > len(inputC):
        for i in range(0, len(inputC)):
            Key += inputK[i]
    if len(inputK) < len(inputC):
        mod = len(inputC) % len(inputK)
        thuong = len(inputC) // len(inputK)
        Key += inputK*thuong
        for i in range(0, mod):
            Key += inputK[i]
    return Key


def autoKey(inputC, inputK):
    Key = inputK
    if len(inputK) > len(inputC):
        for i in range(0, len(inputC)):
            Key += inputK[i]
    if len(inputK) < len(inputC):
        for i in range(0, (len(inputC) - len(inputK))):
            Key += inputC[i]
    return Key


def VigenereLapKey(inputA, inputC, inputK):
    cntOutput = []
    output = ""
    Key = lapKey(inputC, inputK)
    cKey = Ceaser.cInput(inputA, Key)
    cInput = Ceaser.cInput(inputA, inputC)
    for i in range(0, len(cInput)):
        if cInput[i] < 0:
            cntOutput.append(-1)
        else:
            cntOutput.append((cInput[i] - cKey[i]) % 26)
    for j in cntOutput:
        if j < 0:
            output += " "
        else:
            output += inputA[j]
    return output


def VigenereAutoKey(inputA, inputC, inputK, out):
    cntOutput = []
    output = ""
    cKey = Ceaser.cInput(inputA, inputK)
    cInput = Ceaser.cInput(inputA, inputC)
    for i in range(0, len(cKey)):
        if cInput[i] < 0:
            cntOutput.append(-1)
        else:
            cntOutput.append((cInput[i] - cKey[i]) % 26)
    for j in cntOutput:
        if j < 0:
            output += " "
        else:
            output += inputA[j]
    out += output
    if len(inputC) > len(output):
        inputC = inputC[len(output):]
        return VigenereAutoKey(inputA, inputC, output, out)
    elif len(inputC) < len(output) & len(inputC) != 0:
        inputC = inputC[len(inputC):]
        return VigenereAutoKey(inputA, inputC, output, out)
    return out


if __name__ == '__main__':
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    C = input("nhập C : ")
    K = input("nhập K : ")
    C = C.upper()
    K = K.upper()
    x = ""
    print(VigenereLapKey(A, C, K))
    # print(VigenereAutoKey(A, C, K, x))

# wearediscoveredsaveyourself
# deceptive
# ZICVTWQNGKZEIIGASXSTSLVVWLA
# ZICVTWQNGRZGVTWAVZHCQYGLMGJ
