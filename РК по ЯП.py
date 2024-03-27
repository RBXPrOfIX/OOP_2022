from random import randint

def cr_mat(N, M):
    matrix = [[randint(0, 1) for _ in range(M)] for _ in range(N)]
    i, j = randint(0, N-1), randint(0, M-1)
    matrix[i][j] = 2
    if i > 0: matrix[i-1][j] = 1
    return matrix

def gnil(matrix):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    changed = False
    spisok_gnili = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] == 1:
                        spisok_gnili.append((ni, nj))
                        changed = True
    for i, j in spisok_gnili:
        matrix[i][j] = 2
    return changed

def proverka_na_gnil(matrix):
    return all(cell != 1 for row in matrix for cell in row)

def vivod_mat(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

N, M = randint(3, 10), randint(3, 10)
matrix = cr_mat(N, M)

print("Начальная матрица:")
vivod_mat(matrix)

minutes = 0
while True:
    if proverka_na_gnil(matrix):
        print("Минут прошло, как все яблоки стали гнилыми:", minutes)
        break
    if not gnil(matrix):
        print("Невозможно, чтобы все яблоки были гнилыми:", -1)
        break
    minutes += 1
    print(f"Матрица после {minutes} минут(ы):")
    vivod_mat(matrix)
