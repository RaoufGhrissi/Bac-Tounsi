def is_majus(c):
    return ord(c)>=ord('A') and ord(c)<=ord('Z')

def is_minus(c):
    return ord(c)>=ord('a') and ord(c)<=ord('z')

def is_int(c):
    return ord(c)>=ord('0') and ord(c)<=ord('9')

def is_alpha(c):
    return is_majus(c) or is_minus(c)

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
    s = input()
    s=s.upper()
    occ = [0]*26
    nb_total = 0
    for c in s:
        if not is_alpha(c):
           continue
        
        nb_total += 1
        i = char_to_order(c)
        occ[i]+=1
    
    for i in range(26):
        print(occ[i]/nb_total)

main()