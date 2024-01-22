# 문제 설명
# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
#
# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
#
# 제한사항
# a, b, c, d는 1 이상 6 이하의 정수입니다.
#
# 입출력 예
# a | b | c | d | result
# 2 | 2 | 2 | 2 | 2222
# 4 | 1 | 4 | 4 | 1681
# 6 | 3 | 3 | 6 | 27
# 2 | 5 | 2 | 6 | 30
# 6 | 4 | 2 | 5 | 2
#
# 입출력 예 설명
# 입출력 예 #1
# 예제 1번에서 네 주사위 숫자가 모두 2로 같으므로 1111 × 2 = 2222점을 얻습니다. 따라서 2222를 return 합니다.
# 입출력 예 #2
# 예제 2번에서 세 주사위에서 나온 숫자가 4로 같고 나머지 다른 주사위에서 나온 숫자가 1이므로 (10 × 4 + 1)2 = 412 = 1681점을 얻습니다. 따라서 1681을 return 합니다.
# 입출력 예 #3
# 예제 3번에서 a, d는 6으로, b, c는 3으로 각각 같으므로 (6 + 3) × |6 - 3| = 9 × 3 = 27점을 얻습니다. 따라서 27을 return 합니다.
# 입출력 예 #4
# 예제 4번에서 두 주사위에서 2가 나오고 나머지 다른 두 주사위에서 각각 5, 6이 나왔으므로 5 × 6 = 30점을 얻습니다. 따라서 30을 return 합니다.
# 입출력 예 #5
# 예제 5번에서 네 주사위 숫자가 모두 다르고 나온 숫자 중 가장 작은 숫자가 2이므로 2점을 얻습니다. 따라서 2를 return 합니다.


def solution(a, b, c, d):
    num_list = [a, b, c, d]
    num_set = set(num_list)
    num_set_len = len(num_set)
    num_set_list = list(num_set)
    if num_set_len == 1:
        return 1111 * a
    elif num_set_len == 2:
        if num_list.count(num_set_list[0]) == 3:
            return (10 * num_set_list[0] + num_set_list[1]) ** 2
        elif num_list.count(num_set_list[0]) == 1:
            return (10 * num_set_list[1] + num_set_list[0]) ** 2
        else:
            return (num_set_list[0] + num_set_list[1]) * abs(
                num_set_list[0] - num_set_list[1]
            )
    elif num_set_len == 3:
        if num_list.count(num_set_list[0]) == 2:
            return num_set_list[1] * num_set_list[2]
        elif num_list.count(num_set_list[1]) == 2:
            return num_set_list[0] * num_set_list[2]
        else:
            return num_set_list[0] * num_set_list[1]
    elif num_set_len == 4:
        return min(num_list)


# SOL 1
def solution(a, b, c, d):
    l = [a, b, c, d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111 * a
    elif max(c) == 3:
        return (10 * l[c.index(3)] + l[c.index(1)]) ** 2
    elif max(c) == 2:
        if min(c) == 1:
            return eval("*".join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)


# SOL 2
def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums)


# SOL 3
def solution(a, b, c, d):
    answer = 0
    if a == b == c == d:
        answer = 1111 * a
    elif a == b == c:
        answer = (10 * a + d) ** 2
    elif a == b == d:
        answer = (10 * a + c) ** 2
    elif a == c == d:
        answer = (10 * a + b) ** 2
    elif b == c == d:
        answer = (10 * d + a) ** 2
    elif a == b and c == d:
        answer = (a + c) * abs(a - c)
    elif a == c and b == d:
        answer = (a + b) * abs(a - b)
    elif a == d and b == c:
        answer = (a + b) * abs(a - b)
    elif a == b:
        answer = c * d
    elif a == c:
        answer = b * d
    elif a == d:
        answer = b * c
    elif b == c:
        answer = a * d
    elif b == d:
        answer = a * c
    elif c == d:
        answer = a * b
    else:
        answer = min(a, b, c, d)

    return answer
