# 문제 설명
# 음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
# 이 사실을 이용하여 음이 아닌 정수가 문자열 number로 주어질 때, 이 정수를 9로 나눈 나머지를 return 하는 solution 함수를 작성해주세요.
#
# 제한사항
# 1 ≤ number의 길이 ≤ 100,000
# number의 원소는 숫자로만 이루어져 있습니다.
# number는 정수 0이 아니라면 숫자 '0'으로 시작하지 않습니다.
#
# 입출력 예
# number                 | result
# "123"                  | 6
# "78720646226947352489" | 2
#
# 입출력 예 설명
# 입출력 예 #1
# 예제 1번의 number는 123으로 각 자리 숫자의 합은 6입니다. 6을 9로 나눈 나머지는 6이고, 실제로 123 = 9 × 13 + 6입니다. 따라서 6을 return 합니다.
# 입출력 예 #2
# 예제 2번의 number는 78720646226947352489으로 각자리 숫자의 합은 101입니다. 101을 9로 나눈 나머지는 2이고, 실제로 78720646226947352489 = 9 × 8746738469660816943 + 2입니다. 따라서 2를 return 합니다.


def solution(number):
    return int(number) % 9


# SOL 1
def solution(number):
    return sum(list(map(int, number))) % 9


# https://stackoverflow.com/questions/40015439/why-does-map-return-a-map-object-instead-of-a-list-in-python-3
#
# I think the reason why map still exists at all when [generator expressions](https://www.python.org/dev/peps/pep-0289/) also exist, is that it can take multiple iterator arguments that are all looped over and passed into the function:
#    >>> list(map(min, [1,2,3,4], [0,10,0,10]))
#    [0,2,0,4]
#
# That's slightly easier than using zip:
#    >>> list(min(x, y) for x, y in zip([1,2,3,4], [0,10,0,10]))
#
# Otherwise, it simply doesn't add anything over generator expressions.
