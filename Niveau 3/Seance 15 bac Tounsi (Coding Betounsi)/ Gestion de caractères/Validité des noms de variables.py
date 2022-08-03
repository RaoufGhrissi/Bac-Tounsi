def is_majus(c):
    return ord(c)>=ord('A') and ord(c)<=ord('Z')

def is_minus(c):
    return ord(c)>=ord('a') and ord(c)<=ord('z')

def is_int(c):
    return ord(c)>=ord('0') and ord(c)<=ord('9')

def is_alpha(c):
    return is_majus(c) or is_minus(c)

def main():
    n = int(input())
    for i in range(n):
        ch = input()
        first_char = ch[0]
        is_valid_name = is_alpha(first_char) or first_char == '_' # soit true soit false
        
        if not is_valid_name:
            print('NO')
            continue
        else:
            for i in ch:
                if not (is_alpha(i) or is_int(i) or i == '_'):# idha mahouch wehed fi les 3 conditions hedhom
                    is_valid_name = False
                    break
    
        if not is_valid_name:
            print('NO')
        else:
            print('YES')
main()