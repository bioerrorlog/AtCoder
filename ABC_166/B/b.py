n, k = map(int, input().split())
l_n = [0] * n
for i in range(0, k):
    d = int(input())
    a = map(int, input().split())
    for l in a:
        l_n[l-1] = 1
print(l_n.count(0)) 