from Modulo.Logarit import CanNguyenThuy
from Modulo.PhanDuTrungHoa import Euler


# tim log(A)B mod N ( với A là cơ số ở duới B)
def checkLog(A, B, N):
    cnt = 0
    lsMod = []
    if CanNguyenThuy.checkCanNguyenThuy(A, N):
        for i in range(0, N):
            lsMod.append(Euler.printEuler(A, i, N))
            if B == lsMod[i]:
                cnt = i
        return cnt
    else:
        return "a không phải là căn nguyên thủy của n"


if __name__ == '__main__':
    inputA = int(input("nhập a : "))
    inputB = int(input("nhập b : "))
    inputN = int(input("nhập n : "))
    print(checkLog(inputA, inputB, inputN))
