def rotate_number_by_k(N, K):

    num = str(N)
    length = len(num)

    if K > 0:
        rotated = num[K:] + num[:K]
        print(int(rotated))
    else:
        K = abs(K)
        rotated = num[length - K:] + num[:length - K]
        print(int(rotated))

if __name__ == "__main__":
    N = 12345
    K = 2

    rotate_number_by_k(N, K)   
