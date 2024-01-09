# 문제 설명
# 문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.
# 두 수가 n과 m이라면
# ">", "=" : n >= m
# "<", "=" : n <= m
# ">", "!" : n > m
# "<", "!" : n < m
# 두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다. 그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.
#
# 제한 사항
# 1 ≤ n, m ≤ 100
#
# 입출력 예
# ineq | eq  | n  | m  | result
# "<"  | "=" | 20 | 50 | 1
# ">"  | "!" | 41 | 78 | 0
#
# 입출력 예 설명
# 입출력 예 #1
# 20 <= 50은 참이기 때문에 1을 return합니다.
# 입출력 예 #2
# 41 > 78은 거짓이기 때문에 0을 return합니다.


def solution(ineq, eq, n, m):
    if ineq == ">":
        if eq == "=":
            answer = n >= m
        else:
            answer = n > m
    else:
        if eq == "=":
            answer = n <= m
        else:
            answer = n < m
    return int(answer)


# SOL 1
def solution(ineq, eq, n, m):
    return int(eval(str(n) + ineq + eq.replace("!", "") + str(m)))


# SOL 2
def solution(ineq, eq, n, m):
    if eq == "!":
        eq = ""
    return int(eval(f"{n} {ineq}{eq} {m}"))


# SOL 3
def solution(ineq, eq, n, m):
    answer = 0
    if n > m and ineq == ">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1

    return answer


# SOL 4
def solution(ineq, eq, n, m):
    answer = 0

    if (ineq, eq) == ("<", "="):
        answer = int(n <= m)
    elif (ineq, eq) == (">", "="):
        answer = int(n >= m)
    elif (ineq, eq) == ("<", "!"):
        answer = int(n < m)
    elif (ineq, eq) == (">", "!"):
        answer = int(n > m)
    else:
        return "wrong input"

    return answer
