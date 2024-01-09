def solution(n, control):
    for i in range(len(control)):
        if control[i] == "w":
            n += 1
        elif control[i] == "s":
            n -= 1
        elif control[i] == "d":
            n += 10
        elif control[i] == "a":
            n -= 10
    return n


# SOL 1
def solution(n, control):
    key = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))
    return n + sum([key[c] for c in control])


# SOL 2
def solution(n, control):
    answer = n
    c = {"w": 1, "s": -1, "d": 10, "a": -10}
    for i in control:
        answer += c[i]
    return answer
