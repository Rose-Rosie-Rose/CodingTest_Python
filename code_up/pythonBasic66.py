"""
정수 3개 입력받아 짝/홀 출력하기

3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

출력
입력된 순서대로 짝(even)/홀(odd)을 줄을 바꿔 출력한다.
"""
num1, num2, num3 = map(int, input().split())
numbers = [num1, num2, num3]

for i in numbers :
    if i % 2 == 0 :
        print("even")
    else :
        print("odd")