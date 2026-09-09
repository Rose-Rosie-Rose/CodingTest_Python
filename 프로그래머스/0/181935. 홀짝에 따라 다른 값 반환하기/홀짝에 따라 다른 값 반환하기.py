def solution(n):
    return (
        sum(number for number in range(1, n + 1) if number % 2 != 0)
        if n % 2 != 0
        else sum(number ** 2 for number in range(1, n + 1) if number % 2 == 0)
    )