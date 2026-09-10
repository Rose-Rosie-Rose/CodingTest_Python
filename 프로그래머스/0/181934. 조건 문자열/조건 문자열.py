def solution(ineq, eq, n, m):
    if eq == "=" and ineq == ">":
        return 1 if n >= m else 0
    elif eq == "=" and ineq == "<":
        return 1 if n <= m else 0
    elif eq == "!" and ineq == ">":
        return 1 if n > m else 0
    elif eq == "!" and ineq == "<":
        return 1 if n < m else 0
            