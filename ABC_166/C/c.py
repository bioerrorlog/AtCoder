import sys
def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    l_n = [True] * n
    for i in range(m):
        a, b = map(int, input().split())
        if h[a-1] == h[b-1]:
            l_n[b-1] = False
            l_n[a-1] = False
        elif h[a-1] <= h[b-1]:
            l_n[a-1] = False
        elif h[a-1] >= h[b-1]:
            l_n[b-1] = False
    print(sum(l_n)) 

if __name__ == '__main__':
    main()