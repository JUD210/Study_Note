# 문제 설명
# 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.
#
# 제한사항
# my_string은 영소문자로만 이루어져 있습니다.
# 1 ≤ my_string의 길이 ≤ 1,000
# queries의 원소는 [s, e]의 형태로 0 ≤ s ≤ e < my_string의 길이를 만족합니다.
# 1 ≤ queries의 길이 ≤ 1,000
#
# 입출력 예
# my_string     | queries                             | result
# "rermgorpsam" | [[2, 3], [0, 7], [5, 9], [6, 10]]   | "programmers"
#
# 입출력 예 설명
# 예제 1번의 my_string은 "rermgorpsam"이고 주어진 queries를 순서대로 처리하면 다음과 같습니다.
# queries | my_string
#         | "rermgorpsam"
# [2, 3]  | "remrgorpsam"
# [0, 7]  | "progrmersam"
# [5, 9]  | "prograsremm"
# [6, 10] | "programmers"
# 따라서 "programmers"를 return 합니다.


def solution(my_string, queries):
    answer = list(my_string)
    for [s, e] in queries:
        if s == 0:
            answer[s : e + 1] = answer[e::-1]
        else:
            answer[s : e + 1] = answer[e : s - 1 : -1]
    return "".join(answer)


# SOL 1
def solution(my_string, queries):
    answer = list(my_string)
    for s, e in queries:
        answer[s : e + 1] = answer[s : e + 1][::-1]
    #   answer[s : e + 1] = reversed(answer[s : e + 1])
    return "".join(answer)


# SOL 2
def solution(my_string, queries):
    for s, e in queries:
        my_string = my_string[:s] + my_string[s : e + 1][::-1] + my_string[e + 1 :]
    return my_string
