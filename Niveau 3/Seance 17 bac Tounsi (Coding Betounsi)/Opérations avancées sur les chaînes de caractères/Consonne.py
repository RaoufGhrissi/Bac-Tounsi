def consonne(i):
    return i not in [ord('a'), ord('e'), ord('i'), ord('o'), ord('u'), ord('y')]

def main():
    for i in range(ord('a'), ord('z') + 1):
        if consonne(i):
            print(chr(i), end=" ")
    
    

main()