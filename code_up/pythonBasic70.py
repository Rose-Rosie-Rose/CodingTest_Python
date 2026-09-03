"""
월 입력받아 계절 출력하기

월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall
"""
season = int(input())

if season == 12 or 1 <= season <= 2 :
    print("winter")
elif 3 <= season <= 5 :
    print("spring")
elif 6 <= season <= 8 :
    print("summer")
elif 9 <= season <= 11 :
    print("fall")