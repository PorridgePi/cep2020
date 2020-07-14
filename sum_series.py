def sum_series(n):
    if n <= 0:
        return n
    else:
        return n + sum_series(n-2)

print(sum_series(11))