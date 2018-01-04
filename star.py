import math

def star(H, num, x, y):
    '''
    num이 3일 때,
      *
     * *
    *****
    의 트리를 그려주고, n이 3*2^k 꼴인 경우, 2를 나눈 n과 함께 새로운 x,y 인덱스를 변수로 받는
    새로운 함수를 Recursive하게 실행.
    '''
    if num == 3:
        H[x][y] = '*'
        H[x+1][y-1] = '*'
        H[x+1][y+1] = '*'
        for i in range(5):
            H[x+2][y-2+i] = '*'
    else:
        new_num = int(num/2)
        star(H, new_num, x, y)
        star(H, new_num, x+new_num, y - new_num)
        star(H, new_num, x+new_num, y + new_num)


if __name__ == "__main__":
    n = int(input("n을 입력하세요: "))

    # 전체 넓이를 계산해준다
    k = int(math.log(n / 3, 2))
    width = 3 * ( 2 ** (k+1)) - 1

    # White Space로 채워진 Matrix를 만들어준다
    H = []
    for i in range(n):
        empty_row = []
        for j in range(width):
            empty_row.append(' ')
        H.append(empty_row)

    # 처음 시작하는 Index를 계산해준다
    x = 0
    y = int((width-1)/2)

    # 원하는 위치에 별이 들어간 함수를 생성해주는 함수를 실행시킨다
    star(H, n, x, y)

    # 행렬을 그려준다
    for i in range(n):
        for j in range(width):
            print(H[i][j], end='')
        print('\n')