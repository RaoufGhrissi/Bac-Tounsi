def main():
    n = int(input())
    arr = []
    for i in range(n):
        a, b = input().split(" ") # a=travail b=work 
        c = b + " " + a # c = work travail
        arr.append(c)
    arr.sort()
    
    for i in arr:
        print(i)
        
            

main()