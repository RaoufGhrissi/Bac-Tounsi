def tri_selection(tab):
    n = len(tab)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if tab[min] > tab[j]:
                min = j
                
        aux = tab[i]
        tab[i] = tab[min]
        tab[min] = aux

    return tab

tab = [9,6,-3,4,7,8,2,-4,0]
 
tri_selection(tab)
 
for i in tab:
    print(i, end=" ")