

def insert_sort(tablica: list):
    for i in range(1, len(tablica)):
        j = i
        while j > 0 and tablica[j-1] > tablica[j]:
            tablica[j], tablica[j-1] = tablica[j-1], tablica[j]
            j = j - 1


tab1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
tab2 = [9, 2, 0]
print(tab1)
insert_sort(tab1)
print(tab1)
print(tab2)
insert_sort(tab2)
print(tab2)
