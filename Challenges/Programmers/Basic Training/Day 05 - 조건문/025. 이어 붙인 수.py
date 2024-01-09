# 문제 설명
# 정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 2 ≤ num_list의 길이 ≤ 10
# 1 ≤ num_list의 원소 ≤ 9
# num_list에는 적어도 한 개씩의 짝수와 홀수가 있습니다.
#
# 입출력 예
# num_list	result
# [3, 4, 5, 2, 1]	393
# [5, 7, 8, 3]	581
#
# 입출력 예 설명
# 입출력 예 #1
# 홀수만 이어 붙인 수는 351이고 짝수만 이어 붙인 수는 42입니다. 두 수의 합은 393입니다.
# 입출력 예 #2
# 홀수만 이어 붙인 수는 573이고 짝수만 이어 붙인 수는 8입니다. 두 수의 합은 581입니다.


def solution(num_list):
    answer = 0
    str_odd, str_even = "", ""
    for i in range(0, len(num_list)):
        if num_list[i] % 2:
            str_odd += str(num_list[i])
        else:
            str_even += str(num_list[i])
    return int(str_odd) + int(str_even)
