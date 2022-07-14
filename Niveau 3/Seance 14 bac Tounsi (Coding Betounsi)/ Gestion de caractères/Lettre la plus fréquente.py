def version1():
    """
    version 1 of problem: find the occurence of char c in string p 
    """
    p = "aabAAAcaaA" #input()
    c = 'a'
    p=p.upper()
    c=c.upper()
    occ=0
    for i in p:
        if i==c:
            occ+=1 
    print(occ)

def char_to_order(c):
    return ord(c)-ord('A')
    """
        A -> 0
        B -> 1 
        .
        .
        Z -> 25
    """

def order_to_char(i):
    return chr(i+ord('A'))
    """
        0 -> A 
        1 -> B
        .
        .
        25 -> Z
    """

def main():
    p = input()
    p=p.upper()
    occ = [0]*26
    
    for c in p:
        if c == ' ':
           continue
          
        i = char_to_order(c)
        occ[i]+=1
    
    maxx=0
    res='A'
    for i in range(26):
        if occ[i]>maxx:
            maxx=occ[i]
            res=order_to_char(i)
    print(res)
main()


