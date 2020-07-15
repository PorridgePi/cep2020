def sum_odd_n(n):
    if n == 1:
        return 1
    else:
        return sum_odd_n(n-1)+2*n-1

print(sum_odd_n(3))