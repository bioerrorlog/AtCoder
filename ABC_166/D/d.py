import sys
input = sys.stdin.readline

def main():
    x = int(input())
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            if x == i**5 - j**5:
                print(i, j)
                break
        else:
            continue
        break

if __name__ == '__main__':
    main()