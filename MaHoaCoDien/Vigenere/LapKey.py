from MaHoaCoDien.Ceaser import Ceaser


def lapKey(inputM, inputK):
    Key = ""
    if len(inputK) > len(inputM):
        for i in range(0, len(inputM)):
            Key += inputK[i]
    if len(inputK) < len(inputM):
        mod = len(inputM) % len(inputK)
        thuong = len(inputM) // len(inputK)
        Key += inputK*thuong
        for i in range(0, mod):
            Key += inputK[i]
    return Key


def autoKey(inputM, inputK):
    Key = inputK
    if len(inputK) > len(inputM):
        for i in range(0, len(inputM)):
            Key += inputK[i]
    if len(inputK) < len(inputM):
        for i in range(0, (len(inputM) - len(inputK))):
            Key += inputM[i]
    return Key


def Vigenere(inputA, inputM, inputK):
    cntOutput = []
    output = ""
    Key = lapKey(inputM, inputK)
    # Key = autoKey(inputM, inputK)
    cKey = Ceaser.cInput(inputA, Key)
    cInput = Ceaser.cInput(inputA, inputM)
    for i in range(0, len(cInput)):
        if cInput[i] < 0:
            cntOutput.append(-1)
        else:
            cntOutput.append((cInput[i] + cKey[i]) % 26)
    for j in cntOutput:
        if j < 0:
            output += " "
        else:
            output += inputA[j]
    return output


if __name__ == '__main__':
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    M = input("nhập M : ")
    K = input("nhập K : ")
    M = M.upper()
    K = K.upper()
    print(Vigenere(A, M, K))

# wearediscoveredsaveyourself
# deceptive
