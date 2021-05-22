N = int(input())

def fibo(n):
    fibo = [2, 1, 1]
    for i in range(3, n + 1):
        fibo[i % 3] = fibo[(i - 1) % 3] + fibo[(i - 2) % 3]
    return fibo[n % 3]

print(fibo(N))
