# inputA = int(input("Nhập a : "))
# inputN = int(input("Nhập n : "))

# tìm nghịch đảo của a mod theo n theo thuật toán euclid


def modAndThuong(A, N):
    lsMod = [N, A]
    lsThuong = [0, 0]
    for i in range(0, 100):
        if lsMod[i + 1] == 0:
            break
        else:
            lsThuong.append(lsMod[i] // lsMod[i + 1])
            lsMod.append(lsMod[i] % lsMod[i + 1])
    if lsMod[-2] != 1:
        return "không có nghịch đảo"
    else:
        return nghichDao(lsThuong, N)


def nghichDao(lsThuong, N):
    cnt = [[1, 0], [0, 1]]
    for i in range(0, len(lsThuong) - 2):
        x = cnt[i][0] - lsThuong[i + 2] * cnt[i + 1][0]
        y = cnt[i][1] - lsThuong[i + 2] * cnt[i + 1][1]
        cnt.append([x, y])
    if cnt[-2][1] < 0:
        cnt[-2][1] += N
    return cnt[-2][1]


if __name__ == '__main__':
    inputA = 135
    inputN = 553
    print("nghịch đảo của a mod n là : ")
    print(modAndThuong(inputA, inputN))
