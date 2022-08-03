def main():
    n = int(input())
    actual = input()
    print(actual)
    for i in range(n-1):
        ch = input()
        if ch>actual:
            print(ch)
            actual = ch
            

main()