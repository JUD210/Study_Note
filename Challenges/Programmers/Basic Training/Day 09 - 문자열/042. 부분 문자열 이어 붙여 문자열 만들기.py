# 문제 설명
# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
#
# 제한사항
# 1 ≤ my_strings의 길이 = parts의 길이 ≤ 100
# 1 ≤ my_strings의 원소의 길이 ≤ 100
# parts[i]를 [s, e]라 할 때, 다음을 만족합니다.
# 0 ≤ s ≤ e < my_strings[i]의 길이
#
# 입출력 예
# my_strings                                            | parts                            | result
# ["progressive", "hamburger", "hammer", "ahocorasick"] | [[0, 4], [1, 2], [3, 5], [7, 7]] | "programmers"
#
# 입출력 예 설명
# 입출력 예 #1
# 예제 1번의 입력을 보기 좋게 표로 나타내면 다음과 같습니다.
# i | my_strings[i]  | parts[i]  | 부분 문자열
# 0 | "progressive"  | [0, 4]    | "progr"
# 1 | "hamburger"    | [1, 2]    | "am"
# 2 | "hammer"       | [3, 5]    | "mer"
# 3 | "ahocorasick"  | [7, 7]    | "s"
# 각 부분 문자열을 순서대로 이어 붙인 문자열은 "programmers"입니다. 따라서 "programmers"를 return 합니다.


def solution(my_strings, parts):
    str_lst = []
    for i in range(0, len(parts)):
        str_lst.append(my_strings[i][parts[i][0] : parts[i][1] + 1])
    return "".join(str_lst)


# SOL 1
# My comment: answer가 문자열로 선언되었는데, 문자열은 immutable 객체이므로 for문을 반복할 때마다 새로운 str을 계속해서 선언하게 됩니다. 이는 비효율적이므로, answer = [] 및 answer.append() 를 사용하면 더 좋을 것 같습니다!
def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s : e + 1]
    return answer


# SOL 2
def solution(my_strings, parts):
    return "".join(
        my_strings[i][parts[i][0] : parts[i][1] + 1] for i in range(len(my_strings))
    )
