def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k


tab = [9,6,-3,4,7,8,2,-4,0]
tri_insertion(tab)

for i in tab:
    print(i, end=" ")