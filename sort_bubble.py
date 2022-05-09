

def bubble_sort(tablica: list):
    for i in range(len(tablica)-1, 0, -1):
        for j in range(0, i):
            if tablica[j] > tablica[j+1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]


tab1 = [3, 2, 1, 4, 5, 6, 5, 4]
print(tab1)
bubble_sort(tab1)
print(tab1)
