def is_majus(c):
    return ord(c)>=ord('A') and ord(c)<=ord('Z')

def is_minus(c):
    return ord(c)>=ord('a') and ord(c)<=ord('z')

def is_int(c):
    return ord(c)>=ord('0') and ord(c)<=ord('9')
 
def is_caracter(c):
    return is_majus(c) or is_minus(c)
    
def to_upper(s):
    a=""
    for i in s:
        if is_minus(i):
            a+=chr(ord(i)-(ord('a')-ord('A')))
        else:
            a+=i
    return a

def to_lower(s):
    a=""
    for i in s:
        if is_majus(i):
            a+=chr(ord(i)+(ord('a')-ord('A')))
        else:
            a+=i
    return a
    
def capitalizze(s):
    c = ""
    ch = ""
    for i in s:
        if i != ' ':
            c += to_lower(i)
        else:
            c = list(c)
            c[0]=to_upper(c[0])
            c = "".join(c)
            ch+=c
            ch+=' '
            c=""
    
    c = list(c)
    c[0]=to_upper(c[0])
    c = "".join(c)
    ch+=c
    return ch
    
def char_to_order(c):
    return ord(c)-ord('a')
    """
        A -> 0
        B -> 1 
        .
        .
        Z -> 25
    """

def order_to_char(i):
    return chr(i+ord('a'))
    """
        0 -> A 
        1 -> B
        .
        .
        25 -> Z
    """

def cryptage(c, d):
    i = char_to_order(c) # 0->25
    a = i+d # c > 25 or c < 0
    b = a % 26
    res = order_to_char(b)
    return res

def main():
    n = int(input())
    for i in range(2, n+1):
        s = input()
        d = -5*i
        if i%2 == 0:
            d = 3*i;
        res = ""
        for c in s:
            if not is_caracter(c):
                res += c
            else:
                if is_majus(c):
                    j = to_lower(c)
                    x = cryptage(j,-d)
                    res += to_upper(x)
                else:
                    res += cryptage(c,-d)
        print(res)


main()