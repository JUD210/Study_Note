# 제한사항
# my_string은 숫자와 알파벳으로 이루어져 있습니다.
# 1 ≤ my_string의 길이 ≤ 1,000
# 1 ≤ n ≤ my_string의 길이
#
# 입출력 예
# my_string         | n   | result
# "ProgrammerS123"  | 11  | "grammerS123"
# "He110W0r1d"      | 5   | "W0r1d"
#
# 입출력 예
# 입출력 예 #1
# 예제 1번의 my_string에서 뒤의 11글자는 "grammerS123"이므로 이 문자열을 return 합니다.
# 입출력 예 #2
# 예제 2번의 my_string에서 뒤의 5글자는 "W0r1d"이므로 이 문자열을 return 합니다.


def solution(my_string, n):
    return "".join(my_string[-1 : -n - 1 : -1][::-1])


# SOL 1
def solution(my_string, n):
    return my_string[-n:]


# SOL 2
solution = lambda my_string, n: my_string[len(my_string) - n :]
