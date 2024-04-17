
def cInput(inputA, inputM):
    cntInput = []
    for j in range(0, len(inputM)):
        if inputM[j] != " ":
            cntInput.append(inputA.find(inputM[j]))
        else:
            cntInput.append(-1)
    return cntInput


def cOutput(inputA, inputM, inputK):
    cntInput = cInput(inputA, inputM)
    cntOutput = []
    for i in range(0, len(cntInput)):
        if cntInput[i] < 0:
            cntOutput.append(-1)
        else:
            cntOutput.append((cntInput[i] + inputK) % 26)
    return cntOutput


def ceaser(inputA, inputM, inputK):
    C = ""
    cntOutput = cOutput(inputA, inputM, inputK)
    for j in cntOutput:
        if j < 0:
            C += " "
        else:
            C += inputA[j]
    return C


if __name__ == '__main__':
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    M = input("nhập M : ")
    K = int(input("nhập K : "))
    M = M.upper()
    print(ceaser(A, M, K))
