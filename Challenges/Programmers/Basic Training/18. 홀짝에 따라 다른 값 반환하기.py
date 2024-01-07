# 문제 설명
# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
#
# 제한사항
# 1 ≤ n ≤ 100
#
# 입출력 예
# n  | result
# 7  | 16
# 10 | 220
#
# 입출력 예 설명
# 입출력 예 #1
# 예제 1번의 n은 7로 홀수입니다. 7 이하의 모든 양의 홀수는 1, 3, 5, 7이고 이들의 합인 1 + 3 + 5 + 7 = 16을 return 합니다.
# 입출력 예 #2
# 예제 2번의 n은 10으로 짝수입니다. 10 이하의 모든 양의 짝수는 2, 4, 6, 8, 10이고 이들의 제곱의 합인 22 + 42 + 62 + 82 + 102 = 4 + 16 + 36 + 64 + 100 = 220을 return 합니다.


def solution(n):
    answer = 0
    if n % 2:
        for i in range(1, n + 1, 2):
            answer += i
    else:
        for i in range(2, n + 1, 2):
            answer += i * i
    return answer


# SOL 1
# def solution(n):
#     if n % 2:
#         return sum(range(1, n + 1, 2))
#     return sum([i * i for i in range(2, n + 1, 2)])

# SOL 2
# def solution(n):
#     return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)
