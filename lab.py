def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)
x=int(input())
while True:
    if x == 0:
        break
    else:
        print(fact(x))
    break