def is_majus(c):
    return ord(c)>=ord('A') and ord(c)<=ord('Z')

def is_minus(c):
    return ord(c)>=ord('a') and ord(c)<=ord('z')

def is_int(c):
    return ord(c)>=ord('0') and ord(c)<=ord('9')
 
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
    
def get_book_acc(s):
    ac = ""
    c = ""
    for i in s:
        if i != ' ':
            c += i
        else:
            ac += c[0]
            c = ""
    ac += c[0]
    return ac

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

def main():
    ac = input()
    n = int(input())
    for i in range(n):
        s = input()
        s = capitalizze(s)
        acc = get_book_acc(s)
        if (ac == acc):
           print(s)

main()