"""
정수 2개 입력받아 큰 값 출력하기

입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.

출력
두 정수 중 큰 값을 10진수로 출력한다.
"""
num1, num2 = map(int, input().split())

if num1 > num2 :
    print(num1)
else :
    print(num2)