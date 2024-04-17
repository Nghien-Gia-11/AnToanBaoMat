if __name__ == '__main__':
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    C = input("nhập C : ")
    K = input("nhập K : ")
    M = ""
    C = C.upper()
    K = K.upper()
    cnt = []
    for i in range(0, len(C)):
        if C[i] in K:
            cnt.append(K.index(C[i]))
    for i in cnt:
        M += A[i]
    print(M)

# M = AWOMANGIVESANDFO
# K = THLEYNPSXADWKFUBOGMQVJRCIZ
# C = TRUKTFPXJYMTFENU
