"""
비트단위로 AND 하여 출력하기

입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)

출력
두 정수를 비트단위(bitwise)로 and 계산을 수행한 결과를 10진수로 출력한다.
"""

num1, num2 = map(int, input().split())

print(num1 & num2)