
def cInput(inputA, inputC):
    cntInput = []
    for j in range(0, len(inputC)):
        if inputC[j] != " ":
            cntInput.append(inputA.find(inputC[j]))
        else:
            cntInput.append(-1)
    return cntInput


def cOutput(inputA, inputC, inputK):
    cntInput = cInput(inputA, inputC)
    cntOutput = []
    for i in range(0, len(cntInput)):
        if cntInput[i] < 0:
            cntOutput.append(-1)
        else:
            cntOutput.append((cntInput[i] - inputK) % 26)
    return cntOutput


def ceaser(inputA, inputC, inputK):
    M = ""
    cntOutput = cOutput(inputA, inputC, inputK)
    for j in cntOutput:
        if j < 0:
            M += " "
        else:
            M += A[j]
    return M


if __name__ == '__main__':
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    C = input("nhập C : ")
    K = int(input("nhập K : "))
    C = C.upper()
    print(ceaser(A, C, K))
