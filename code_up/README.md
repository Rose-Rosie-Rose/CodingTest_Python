# PYTHON 문법 정리
---
#### 비트단위(bitwise)연산자
- `~`(bitwise not)
- `&`(bitwise and)
- `|`(bitwise or)
- `^`(bitwise xor)
- `<<`(bitwise left shift)
- `>>`(bitwise right shift)

---
#### ord() 함수
- 문자 -> 숫자
- print(ord("a")) => 97
  print(ord("b")) => 98

---
#### 수열
어떤 순서대로 나열된 숫자들

#### 등비수열
a: 시작값(첫째항) r: 공비(비율) n: 구하려는 순서
result = a * (r ** (n - 1))