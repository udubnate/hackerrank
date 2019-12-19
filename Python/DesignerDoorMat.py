N,M = input().split()


def doormat(N,M):
    for i in range(int(N)):
        # top mat
        if i < (int(N)-1)/2:
            length = i*2+1
            graphic = '.|.'*length
            print(graphic.center(int(M),'-'))
        # welcome message
        elif i == (int(N)-1)/2:
            print("WELCOME".center(int(M), '-'))
        # bottom mat
        else:
            length = (int(N) - i)*2-1
            graphic = '.|.'*length
            print(graphic.center(int(M),'-'))

doormat(N,M)


