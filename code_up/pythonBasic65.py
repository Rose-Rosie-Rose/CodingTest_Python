"""
정수 3개 입력받아 짝수만 출력하기

3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

출력
짝수만 순서대로 줄을 바꿔 출력한다.
"""
num1, num2, num3 = map(int, input().split())

if num1 % 2 == 0 :
    print(num1)
if num2 % 2 == 0 :
    print(num2)
if num3 % 2 == 0 :
    print(num3)