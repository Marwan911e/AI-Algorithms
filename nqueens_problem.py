def mark_unsafe(i, j, unsafe_places):
    for k in range(4):
        unsafe_places[k][j] = 1
        unsafe_places[i][k] = 1
    for k in range(4):
        if i + k < 4 and j + k < 4:
            unsafe_places[i + k][j + k] = 1
        if i - k >= 0 and j - k >= 0:
            unsafe_places[i - k][j - k] = 1
        if i + k < 4 and j - k >= 0:
            unsafe_places[i + k][j - k] = 1
        if i - k >= 0 and j + k < 4:
            unsafe_places[i - k][j + k] = 1

def add_queen(i, j, unsafe_places):
    global queens

    matrix[i][j] = 1
    mark_unsafe(i, j, unsafe_places)

    queens -= 1

    for i in range(4):
        for j in range(4):
            if unsafe_places[i][j] == 0:
                add_queen(i, j, unsafe_places)
                

queens = 4
for i in range(4):
    if queens > 0:
        matrix = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        unsafe_places = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        queens = 4
        add_queen(0, i, unsafe_places)


for i in range(4):
    for j in range(4):
        if j < 3:
            print(matrix[i][j], end=", ")
        else:
            print(matrix[i][j], end=" ")

    print()


