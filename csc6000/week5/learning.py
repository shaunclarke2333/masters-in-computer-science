def factorial_calc(num):
    factorial = 1
    for i in range(1,num+1):
        factorial*=i
    # print(f"{factorial}")
    return factorial

n = 200
k = 50
n_minus_k = n - k

print(factorial_calc(n)/factorial_calc(k)*factorial_calc(n_minus_k))