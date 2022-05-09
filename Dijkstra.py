import math

macierz_sasiedztwa_1 = [[0, 3, 0, 3, 5],
                        [3, 0, 5, 1, 0],
                        [0, 5, 0, 2, 0],
                        [3, 1, 2, 0, 1],
                        [5, 0, 0, 1, 0]]

macierz_sasiedztwa_2 = [[0, 3, 0, 0, 3, 0],
                        [0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 3, 0, 1],
                        [0, 3, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 2],
                        [0, 0, 0, 1, 0, 0]]


def dijkstra(macierz, wierzcholek_startu):
    print("Macierz sasiedztwa wyglada nastepujaco: ")
    for x in range(len(macierz)):
        print(macierz[x])
    # tablica mowiaca o poprzedniku prowadzacym do konkretnego wezla
    poprzednicy = [-1] * len(macierz)
    # tablica mowiaca o koszcie drogi z wezla poprzedniego
    klucze = [math.inf] * len(macierz)
    # kolejka priorytetowa na podstawie ktorej bedzie wybierany najstepny krok
    kp = []
    # ustawienie drogi 0 dla elementu startowego
    klucze[wierzcholek_startu] = 0
    # dodajemy wszystkie wierzcholki do kolejki (numer wierzcholka, waga drogi z poprzednika)
    for x in range(len(macierz)):
        kp.append([x, klucze[x]])
    # jesli kolejka nie jest pusta
    while kp:
        # znajduje najmniejszy element (odleglosc) w kolejce
        kp.sort(key=lambda drugi: drugi[1])
        # wybieram pierwszy wierzcholek z posortowanje tablicy ktorego bede teraz sprawdzal
        wierzcholek = kp[0][0]
        # usuwam go
        kp.pop(0)
        # numer wierzcholka do ktorego droge sprawdzamy
        nr_wierzch = 0
        for x in macierz[wierzcholek]:
            # czy istnieje sciezka do tego wierzcholka (waga wieksza niz zero)
            if x > 0:
                # czy nowa droga jest lepsza od poprzednio znalezionej
                if klucze[wierzcholek] + x < klucze[nr_wierzch]:
                    # aktualizuje odleglosc
                    klucze[nr_wierzch] = klucze[wierzcholek] + x
                    # aktualizuje poprzednika
                    poprzednicy[nr_wierzch] = wierzcholek
                    # aktualizuje odleglosc w kolejce priorytetowej
                    for y in kp:
                        if y[0] == nr_wierzch:
                            y[1] = klucze[wierzcholek] + x
            nr_wierzch += 1
    print("-----------------------")
    print("Wyniki")
    print("-----------------------")
    print("Poprzednicy: ")
    print(poprzednicy)
    print("Wagi: ")
    print(klucze)
    print("=======================")


dijkstra(macierz_sasiedztwa_1, 0)
dijkstra(macierz_sasiedztwa_2, 0)
