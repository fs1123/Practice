def prime(n):
    # n까지 소수 리스트를 구한다.
    prime_list = []
    number_list = list(range(2,10001))

    while number_list:
        prime_list.append(number_list[0])
        number_list = list(num for num in number_list if num % number_list[0] != 0 )

    return prime_list


def goldbach(n, prime_list):
    # 가장 차이가 작은 소수 두개를 찾아야 하므로 중간지점부터 찾아주면 된다
    i = j = n // 2
    while True:
        if i in prime_list and j in prime_list:
            print(i,j)
            break
        i -= 1
        j += 1


if __name__ == '__main__':
    M = int(input())
    test_cases = []
    for i in range(M):
        n = int(input())
        test_cases.append(n)

    prime_list = prime(10000)
    for num in test_cases:
        goldbach(num, prime_list)
