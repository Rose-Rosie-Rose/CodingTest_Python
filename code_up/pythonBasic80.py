"""
주사위 2개 던지기

1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
나올 수 있는 모든 경우를 출력해보자.

"""
dice1, dice2 = map(int, input().split())

for d1 in range(1, dice1 + 1):
    for d2 in range(1, dice2 + 1):
        print(d1, d2)