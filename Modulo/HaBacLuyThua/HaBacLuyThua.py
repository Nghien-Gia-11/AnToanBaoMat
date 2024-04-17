# tính mod b = A^N mod M theo cách hạ bậc
import math


inputA = int(input("nhập a : "))
inputN = int(input("nhập n : "))
inputM = int(input("nhập m : "))

logN = int(math.log2(inputN))
phanDu = []

for i in range(0, logN):
    mod = inputN % 2
    phanDu.append([inputN, mod])
    inputN //= 2

phanDuRever = []
for i in range(len(phanDu) - 1, -1, -1):
    phanDuRever.append(phanDu[i])
print(phanDuRever)


lsMod = [inputA]
for i in range(0, len(phanDuRever)):
    print(phanDuRever[i][0])
    if phanDuRever[i][1] == 1:
        modM = ((lsMod[i] ** 2) % inputM * (inputA % inputM)) % inputM
    else:
        modM = (lsMod[i] ** 2) % inputM
    lsMod.append(modM)
print(lsMod)


# 78
# 39 * 2
# 19 * 2 + 1
# 9 * 2 + 1
# 4 * 2 + 1
# 2 * 2
# 36
# 78
# 287
