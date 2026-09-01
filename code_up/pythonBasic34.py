"""
정수 2개 입력받아 차 계산하기

정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

예시
...
c = a - b
print(c)

참고
수 - 수는 차(subtraction)가 계산된다.

출력
첫 번째 정수에서 두 번째 정수를 뺀 차를 출력한다.
"""
data1, data2 = map(int, input().split())

print(data1 - data2)
