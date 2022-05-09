

def quick_sort(tab: list, first: int, last: int):
    """Implementacja algorytmu quicksort w oparciu o podział Hoare'a oraz pivot wybrany z mediany trzech"""
    if first < last:
        p = partition(tab, first, last)
        quick_sort(tab, first, p)
        quick_sort(tab, p+1, last)


def partition(tab: list, first: int, last: int) -> int:
    """Funkcja ta ustawia wszystkie elementy wieksze od wartosci pivotu po prawej oraz mnijesze po lewej"""
    piv = pivot_mediana3(tab, first, last)
    i = first - 1
    j = last + 1
    while True:
        while True:
            i = i + 1
            if not tab[i] < piv:
                break
        while True:
            j = j - 1
            if not tab[j] > piv:
                break
        if i >= j:
            return j
        tab[i], tab[j] = tab[j], tab[i]


def pivot_mediana3(tab: list, first: int, last: int) -> int:
    """Funkcja zwraca mediane z elementu pierwszego, ostatniego i srodkowego danej tablicy(wycinka),
    również sortuje te elementy"""
    mid = int((first+last)/2)
    if tab[mid] < tab[first]:
        tab[mid], tab[first] = tab[first], tab[mid]
    if tab[last] < tab[first]:
        tab[last], tab[first] = tab[first], tab[last]
    if tab[mid] < tab[last]:
        tab[mid], tab[last] = tab[last], tab[mid]
    return tab[mid]


tab1 = [7, 6, 5, 4, 3, 2, 1, 0]
tab2 = [3, 0, 2, 0, 5, 0, 1, 0, 7]
print(tab1)
quick_sort(tab1, 0, len(tab1)-1)
print(tab1)
print(tab2)
quick_sort(tab2, 0, len(tab2)-1)
print(tab2)
