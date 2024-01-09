# 문제 설명
# 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
# 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.
#
# 제한사항
# 1 ≤ str1, str2의 길이 ≤ 10
#
# 입출력 예
# 입력 #1
# apple pen
# 출력 #1
# applepen
#
# 입력 #2
# Hello World!
# 출력 #2
# HelloWorld!

str1, str2 = input().strip().split(" ")
print(f"{str1}{str2}")


# SOL 1
print(input().strip().replace(' ', ''))

# SOL 2
str1, str2 = input().strip().split(' ')
print(str1, str2, sep='')
