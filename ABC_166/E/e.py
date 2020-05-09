import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    c = [0] * n
    s = 0
    for i, a in enumerate(a_list):
        if i+a < n:
            c[i+a] += 1
        if i-a >= 0:
            s += c[i-a]
    print(s)

if __name__ == '__main__':
    main()