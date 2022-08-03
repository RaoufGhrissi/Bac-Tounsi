
def my_sort(ch):
    #to implement next week
    pass

def main():
    n = int(input())
    arr = []
    for i in range(n):
        ch = input()
        arr.append(ch)
    
    arr.sort()
    
    for i in arr:
        print(i)

main()