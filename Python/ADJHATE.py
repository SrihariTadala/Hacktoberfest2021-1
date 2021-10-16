# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))
    a.sort()
    b = [i for i in a if i%2]
    c = [i for i in a if i%2==0]
    odd, even = len(b), len(c)
    if odd==0 or even==0:
        print(-1)
    else:
        print(*b, *c)
