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

def main():
    ch = input()
    s = input()
    ch = to_lower(ch)
    s = to_lower(s)
    l = str_to_list(s)
    cnt=0
    for i in l:
        if i==ch:
            cnt+=1
    
    print(cnt)
    

main()