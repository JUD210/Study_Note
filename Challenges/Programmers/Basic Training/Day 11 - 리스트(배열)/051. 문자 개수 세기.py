# 문제 설명
# 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.
#
# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000
#
# 입출력 예
# my_string     | result
# "Programmers" | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]
#
# 입출력 예 설명
# 입출력 예 #1
# 예제 1번의 my_string에서 'P'가 1개, 'a'가 1개, 'e'가 1개, 'g'가 1개, 'm'이 2개, 'o'가 1개, 'r'가 3개, 's'가 1개 있으므로 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]를 return 합니다.


# fmt: off
def solution(my_string):
    char_cnt_dict = {
        'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'G' : 0,
        'H' : 0, 'I' : 0, 'J' : 0, 'K' : 0, 'L' : 0, 'M' : 0, 'N' : 0,
        'O' : 0, 'P' : 0, 'Q' : 0, 'R' : 0, 'S' : 0, 'T' : 0, 'U' : 0,
        'V' : 0, 'W' : 0, 'X' : 0, 'Y' : 0, 'Z' : 0,
        'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0,
        'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0,
        'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0,
        'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0,
    }
    for c in my_string:
        char_cnt_dict[c] += 1
    answer = []
    for c in char_cnt_dict:
        answer.append(char_cnt_dict[c])
    return answer
# fmt: on


# SOL 1
def solution(my_string):
    answer = [0] * 52
    for x in my_string:
        if x.isupper():
            answer[ord(x) - 65] += 1
        else:
            answer[ord(x) - 71] += 1
    return answer


# SOL 2
def solution(my_string):
    return [
        my_string.count(alphabet)
        for alphabet in "abcdefghijklmnopqrstuvwxyz".upper()
        + "abcdefghijklmnopqrstuvwxyz"
    ]
