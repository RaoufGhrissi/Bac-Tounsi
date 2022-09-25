def tri_shell(tab, h):
    n = len(tab)
    for i in range(1, n): 
        k = tab[i]
        j = i-h
        while j >= 0 and k < tab[j]: 
            tab[j + h] = tab[j]
            j -= h
        tab[j + h] = k


hs = []
h = 1
tab = [9,6,-3,4,7,8,2,-4,0]
n = len(tab)

while h<=n:
    hs.append(h)
    h = 3*h+1

hs.reverse()
for h in hs:
    tri_shell(tab, h)

for i in tab:
    print(i, end=" ")