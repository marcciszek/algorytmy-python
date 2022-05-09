import math

distance = [[0, 1, 5, math.inf, math.inf, math.inf, math.inf],
            [math.inf, 0, 2, math.inf, math.inf, math.inf, math.inf],
            [math.inf, math.inf, 0, math.inf, math.inf, math.inf, math.inf],
            [7, math.inf, math.inf, 0, 1, math.inf, math.inf],
            [math.inf, math.inf, math.inf, math.inf, 0, 1, math.inf],
            [2, math.inf, math.inf, 4, math.inf, 0, math.inf],
            [6, math.inf, math.inf, math.inf, math.inf, 3, 0]]

prev = [[0, 1, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 5, 0],
        [6, 0, 0, 6, 0, 0, 0],
        [7, 0, 0, 0, 0, 7, 0]]


def floyd_warshall(d_odleglosci, p_poprzednicy):
    rozmiar = len(d_odleglosci)
    for u in range(rozmiar):
        for v in range(rozmiar):
            if v == u:
                continue
            else:
                for w in range(rozmiar):
                    if w == v or w == u:
                        continue
                    else:
                        nowa_droga = d_odleglosci[v][u] + d_odleglosci[u][w]
                        if nowa_droga < d_odleglosci[v][w]:
                            d_odleglosci[v][w] = nowa_droga
                            p_poprzednicy[v][w] = p_poprzednicy[u][w]
    print("-----------------------")
    for x in range(len(d_odleglosci)):
        print(d_odleglosci[x])
    print("-----------------------")
    for x in range(len(p_poprzednicy)):
        print(p_poprzednicy[x])

floyd_warshall(distance, prev)
