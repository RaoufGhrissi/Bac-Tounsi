def char_to_order(first_char):
    return ord(first_char)-ord('A')

def calcul_nombre(nom):
    nombre=0;
    for char in nom:
        nombre+=char_to_order(char)
    while(nombre>9): # nombre>=10 
        nombreAsStr = str(nombre)
        nombre=0;
        for i in nombreAsStr:
            nombre+=ord(i)-ord('0')
    return nombre
            
def main():
    nom1, nom2 = map(str, input().split(" "))
    """noms = input().split(" ") # list of 2 names
    nom1 = noms[0]
    nom2 = noms[1]"""
    n1=calcul_nombre(nom1)
    n2=calcul_nombre(nom2)
    
    print(n1, end=" ")
    print(n2)

        
main()