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
    
def str_to_list(s):
    c = ""
    l = []
    for i in s:
        if i != ' ':
            c += i
        else:
            l.append(c)
            c = ""
    l.append(c)
    return l

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
        l = str_to_list(s)
        if len(l) != len(ac):
            continue
        ok = True
        for j in range(len(l)):
            if l[j][0] != ac[j]:
                ok = False
                break
            
        if ok:
            print(s)
    

main()