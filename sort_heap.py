

def heap_sort(tab: list):
    n = len(tab)

    for i in range(n//2-1, -1, -1):
        heapify(tab, i, n)

    for i in range(n-1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab, 0, i)


def heapify(tab: list, i: int, m: int):
    maximum = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < m and tab[left] > tab[i]:
        maximum = left
    if right < m and tab[right] > tab[maximum]:
        maximum = right
    if maximum != i:
        tab[i], tab[maximum] = tab[maximum], tab[i]
        heapify(tab, maximum, m)


tab1 = [8, 6, 4, 8, 1, 3, 6]
tab2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(tab1)
heap_sort(tab1)
print(tab1)
print(tab2)
heap_sort(tab2)
print(tab2)
