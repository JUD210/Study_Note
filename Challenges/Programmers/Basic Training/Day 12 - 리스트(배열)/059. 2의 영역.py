# 문제 설명
# 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, arr에 2가 없는 경우 [-1]을 return 합니다.
#
# 제한사항
# 1 ≤ arr의 길이 ≤ 100,000
# 1 ≤ arr의 원소 ≤ 10
#
# 입출력 예
# arr                       | result
# [1, 2, 1, 4, 5, 2, 9]     | [2, 1, 4, 5, 2]
# [1, 2, 1]                 | [2]
# [1, 1, 1]                 | [-1]
# [1, 2, 1, 2, 1, 10, 2, 1] | [2, 1, 2, 1, 10, 2]
#
# 입출력 예 설명
# 입출력 예 #1
# 2가 있는 인덱스는 1번, 5번 인덱스뿐이므로 1번부터 5번 인덱스까지의 부분 배열인 [2, 1, 4, 5, 2]를 return 합니다.
# 입출력 예 #2
# 2가 한 개뿐이므로 [2]를 return 합니다.
# 입출력 예 #3
# 2가 배열에 없으므로 [-1]을 return 합니다.
# 입출력 예 #4
# 2가 있는 인덱스는 1번, 3번, 6번 인덱스이므로 1번부터 6번 인덱스까지의 부분 배열인 [2, 1, 2, 1, 10, 2]를 return 합니다.


def solution(arr):
    start, end = -1, -1
    for i in range(0, len(arr)):
        if arr[i] == 2:
            start = i
            break

    for i in range(0, len(arr)):
        if arr[len(arr) - 1 - i] == 2:
            end = len(arr) - 1 - i
            break

    if start == -1:
        return [-1]
    else:
        return arr[start : end + 1]


# SOL 1
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]


# SOL 2
def solution(arr):
    return [-1] if 2 not in arr else arr[arr.index(2) : len(arr) - arr[::-1].index(2)]


# SOL 3
def solution(arr):
    check = []
    if 2 not in arr:
        return [-1]
    else:
        for i in range(0, len(arr)):
            if arr[i] == 2:
                check.append(i)
    return arr[check[0] : check[-1] + 1]
