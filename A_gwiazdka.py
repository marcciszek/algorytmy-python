import math

macierz_sasiedztwa_1 = [[0, 5, 0, 1, 0, 0, 0, 0],
                        [0, 0, 2, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 3],
                        [0, 0, 0, 0, 1, 2, 0, 0],
                        [0, 0, 4, 0, 0, 0, 0, 0],
                        [4, 0, 0, 0, 0, 0, 2, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 2, 0, 0, 0]]

oszacowane_0_7 = [4, 8, 3, 4, 5, 2, 1, 0]


def a_gwiazdka(macierz, odleglosci_do_celu, wierzcholek_startu, wierzcholek_konca):
    print("Macierz sasiedztwa wyglada nastepujaco: ")
    for x in range(len(macierz)):
        print(macierz[x])

    # przyblizone oszacowane odleglosci
    h = odleglosci_do_celu
    # rzeczywisty koszt od poczadku do konkretnego wezla
    g = [math.inf] * len(macierz)
    # oszacowanie kosztu calej drogi od poczatku do konca przez konkretny wezel
    f = [math.inf]*len(macierz)
    # poprzednik dla najkrotszej drogi dla konkretnego wezla
    poprzednicy = [-1] * len(macierz)

    # usatwienie wartosci poczatkowych (pierwszy wezel)
    g[wierzcholek_startu] = 0
    f[wierzcholek_startu] = h[wierzcholek_startu]

    # tablica zawierajaca wezly do sprawdzenia
    q_wezly_otwarte = []
    # tablica zawierajaca wezly juz sprawdzone
    s_wezly_zamkniete = []

    # dodaj wezel startowy
    q_wezly_otwarte.append([wierzcholek_startu, f[wierzcholek_startu]])

    # jesli tablica wezlow otwartych nie jest pusta
    while q_wezly_otwarte:
        # znalezienie najkorzystniejszego wezla
        q_wezly_otwarte.sort(key=lambda drugi: drugi[1])
        wierzcholek = q_wezly_otwarte[0][0]
        # sprawdzam czy nie jestem na wezle docelowym
        if wierzcholek == wierzcholek_konca:
            break
        # usuwam aktualny wezel z tablicy wezlow otwartych
        do_zamkniecia = q_wezly_otwarte.pop(0)[0]
        # dodaje wezel do tablicy wezlow zamknietych
        s_wezly_zamkniete.append(do_zamkniecia)
        # numer wierzcholka do ktorego droge sprawdzamy
        nr_wierzch = 0
        for waga in macierz[wierzcholek]:
            # czy istnieje sciezka do tego wierzcholka
            if waga > 0:
                # jesli sciezka prowadzi do wezla juz sprawdzonego, pomijam
                if nr_wierzch in s_wezly_zamkniete:
                    nr_wierzch += 1
                    continue
                # czy nowa droga jest lepsza od poprzednio znalezionej
                if macierz[wierzcholek][nr_wierzch] + g[wierzcholek] < g[nr_wierzch]:
                    # aktualizuje poprzednika
                    poprzednicy[nr_wierzch] = wierzcholek
                    # obliczenie rzeczywistego kosztu drogi
                    g[nr_wierzch] = macierz[wierzcholek][nr_wierzch] + g[wierzcholek]
                    # oszacowanie kosztu calej drogi
                    f[nr_wierzch] = g[nr_wierzch] + h[nr_wierzch]
                    # jesli wierzcholka nie ma w tablicy wezlow otwartych to go tam dodaje
                    czy_dodac = True
                    for wezel in q_wezly_otwarte:
                        if wezel[0] == nr_wierzch:
                            czy_dodac = False
                            break
                    if czy_dodac:
                        q_wezly_otwarte.append([nr_wierzch, f[nr_wierzch]])
            nr_wierzch += 1
    print("------------------------")
    print("h: ", h)
    print("g: ", g)
    print("f: ", f)
    print("poprzednicy: ", poprzednicy)


a_gwiazdka(macierz_sasiedztwa_1, oszacowane_0_7, 0, 7)
