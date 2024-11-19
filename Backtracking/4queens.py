def mark_unsafe(i, j, unsafe_places):
    for k in range(4):
        unsafe_places[i][k] = 1
        unsafe_places[k][j] = 1
    for k in range(4):
        if i + k < 4 and j + k < 4:
            unsafe_places[i + k][j + k] = 1
        if i - k >= 0 and j - k >= 0:
            unsafe_places[i - k][j - k] = 1
        if i + k < 4 and j - k >= 0:
            unsafe_places[i + k][j - k] = 1
        if i - k >= 0 and j + k < 4:
            unsafe_places[i - k][j + k] = 1

def add_queen(queens_left, unsafe_places, matrix):
    if queens_left == 0:
        return True
    for i in range(4):
        for j in range(4):
            if unsafe_places[i][j] == 0:
                matrix[i][j] = 1
                new_unsafe_places = [row[:] for row in unsafe_places]
                mark_unsafe(i, j, new_unsafe_places)
                if add_queen(queens_left - 1, new_unsafe_places, matrix):
                    return True
                matrix[i][j] = 0
    return False

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

add_queen(queens, unsafe_places, matrix)

for i in range(4):
        for j in range(4):
            if j < 3:
                print(matrix[i][j], end=", ")
            else:
                print(matrix[i][j], end=" ")
        print()