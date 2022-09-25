def tri_bulle(tab):
    n = len(tab)

    for i in range(n):
        for j in range(n-i-1):
            if tab[j]>tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]


tab = [9,6,-3,4,7,8,2,-4,0]

tri_bulle(tab)

for i in tab:
    print(i, end=" ")