if __name__ == '__main__':
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    M = input("nhập M : ")
    K = input("nhập K : ")
    C = ""
    M = M.upper()
    K = K.upper()
    cnt = []
    for i in range(0, len(M)):
        if M[i] in A:
            cnt.append(A.index(M[i]))
    for i in cnt:
        C += K[i]
    print(C)
# M = AWOMANGIVESANDFO
# K = THLEYNPSXADWKFUBOGMQVJRCIZ
# A = ABCDEFGHIJKLMNOPQRSTUVWXYZ
# C = TRUKTFPXJYMTFENU
