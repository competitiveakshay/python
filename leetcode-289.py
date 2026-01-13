rows = int(input("Enter number of rows: "))
matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

cols = len(matrix[0])

print("Original Matrix")
print()
print(matrix)
print()

def countNeighbours(r, c):
    nei = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if ((i==r and j==c) or i<0 or j<0 or i==rows or j==cols):
                continue

            if matrix[i][j] in [1,3]:
                nei += 1
        
    return nei

for r in range(rows):
    for c in range(cols):
        nei = countNeighbours(r,c)
        if matrix[r][c]:
            if nei in [2,3]:
                matrix[r][c] = 3
        elif nei == 3:
            matrix[r][c] = 2

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 1:
            matrix[r][c] = 0
        elif matrix[r][c] in [2,3]:
            matrix[r][c] = 1

print("New Matrix")
print()
print(matrix)