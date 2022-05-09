

def merge_sort(tab: list, left: int, right: int):
    if left < right:
        mid = (left+right)//2
        merge_sort(tab, left, mid)
        merge_sort(tab, mid+1, right)
        merge(tab, left, mid, right)


def merge(tab: list, left: int, mid: int, right: int):
    q1 = tab[left:mid+1]
    q2 = tab[mid+1:right+1]
    i = left
    while q1 and q2:
        if q1[0] <= q2[0]:
            tab[i] = q1.pop(0)
            i = i + 1
        else:
            tab[i] = q2.pop(0)
            i = i + 1
    while q1:
        tab[i] = q1.pop(0)
        i = i + 1
    while q2:
        tab[i] = q2.pop(0)
        i = i + 1


tab1 = [6, 4, 3, 7, 3, 9, 1, 0]
tab2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(tab1)
merge_sort(tab1, 0, len(tab1)-1)
print(tab1)
print(tab2)
merge_sort(tab2, 0, len(tab2)-1)
print(tab2)
