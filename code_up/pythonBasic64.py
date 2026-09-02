"""
정수 3개 입력받아 가장 작은 값 출력하기

입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.

출력
가장 작은 값을 출력한다.
"""
num1, num2, num3 = map(int, input().split())

if num1 < num2 and num1 < num3 :
    print(num1)
elif num2 < num1 and num2 < num3 :
    print(num2)
else :
    print(num3)