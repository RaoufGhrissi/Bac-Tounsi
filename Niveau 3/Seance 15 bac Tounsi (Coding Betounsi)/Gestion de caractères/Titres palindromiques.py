def is_majus(c):
    return ord(c)>=ord('A') and ord(c)<=ord('Z')

def to_lower(s):
    a=""
    for i in s:
        if is_majus(i):
            a+=chr(ord(i)+(ord('a')-ord('A')))
        else:
            a+=i
    return a

def remove_space(ch):
    s = ""
    for i in ch:
        if i != ' ':
            s+=i
    return s

def is_pal(ch):
    n = len(ch)
    for i in range(n//2):
        if ch[i] != ch[n-1-i]:
            return False
    return True
    
def main():
    n = int(input())

    for i in range(n):
        ch = input()
        original = ch
        ch = remove_space(ch)
        ch = to_lower(ch)
        if is_pal(ch):
            print(original)
        
main()