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

def main():
    cryptage = input()
    text = input()

    s = ""
    for i in text:
        if not is_caracter(i):
            s += i
        else:
            if is_majus(i):
                j = to_lower(i)
                c = cryptage[char_to_order(j)]
                s += to_upper(c)
            else:
                s += cryptage[char_to_order(i)]
    print(s)
    

main()