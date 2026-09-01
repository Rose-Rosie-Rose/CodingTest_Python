"""
실수 2개 입력받아 곱 계산하기

실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

예시
...
m = f1 * f2
print(m)

참고
수 * 수는 곱(multiplication)이 계산된다.

출력
첫 번째 실수와 두 번째 실수를 곱한 값을 출력한다.
"""

data1, data2 = map(float, input().split())

print(data1 * data2)