def main():
    arr = []
    n = int(input())
    
    for nn in range(n):
       ch = input()
       arr.append(ch)
    
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])

main()