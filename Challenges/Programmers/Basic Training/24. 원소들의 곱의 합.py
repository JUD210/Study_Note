# 문제 설명
# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 2 ≤ num_list의 길이 ≤ 10
# 1 ≤ num_list의 원소 ≤ 9
#
# 입출력 예
# num_list	result
# [3, 4, 5, 2, 1]	1
# [5, 7, 8, 3]	0
#
# 입출력 예 설명
# 입출력 예 #1
# 모든 원소의 곱은 120, 합의 제곱은 225이므로 1을 return합니다.
# 입출력 예 #2
# 모든 원소의 곱은 840, 합의 제곱은 529이므로 0을 return합니다.


def solution(num_list):
    res_mul = 1
    for i in range(0, len(num_list)):
        res_mul *= num_list[i]
    return int(res_mul < sum(num_list) ** 2)


# SOL 1
# def solution(num_list):
#     s=sum(num_list)**2
#     m=eval('*'.join([str(n) for n in num_list]))
#     return 1 if s>m else 0
