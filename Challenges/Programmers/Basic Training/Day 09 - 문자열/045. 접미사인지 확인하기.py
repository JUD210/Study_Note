# 문제 설명
# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
#
# 제한사항
# 1 ≤ my_string의 길이 ≤ 100
# 1 ≤ is_suffix의 길이 ≤ 100
# my_string과 is_suffix는 영소문자로만 이루어져 있습니다.
#
# 입출력 예
# my_string | is_suffix   | result
# "banana"  | "ana"       | 1
# "banana"  | "nan"       | 0
# "banana"  | "wxyz"      | 0
# "banana"  | "abanana"   | 0
#
# 입출력 예 설명
# 입출력 예 #1
# 예제 1번에서 is_suffix가 my_string의 접미사이기 때문에 1을 return 합니다.
# 입출력 예 #2
# 예제 2번에서 is_suffix가 my_string의 접미사가 아니기 때문에 0을 return 합니다.
# 입출력 예 #3
# 예제 3번에서 is_suffix가 my_string의 접미사가 아니기 때문에 0을 return 합니다.
# 입출력 예 #4
# 예제 4번에서 is_suffix가 my_string의 접미사가 아니기 때문에 0을 return 합니다.


def solution(my_string, is_suffix):
    suffix_lst = [my_string[i:] for i in range(0, len(my_string))]
    return int(is_suffix in suffix_lst)


# SOL 1
def solution(m, s):
    if m[-len(s) :] == s:
        return 1
    return 0


# SOL 2
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))
