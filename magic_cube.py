import numpy as np

# Function to rotate the matrix
# 90 degree clockwise
def rotateCube(A):
    N = 3
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp


# magicCube=[[8,1,6],[3,5,7],[4,9,2]]
# rotateCube(magicCube)
# print(magicCube)

def reflectCube(A):
    for i in range(3):
        hold = A[i][0]
        A[i][0]=A[i][-1]
        A[i][-1]=hold


def allMagicCube():
    allPoMcs=[]
    magicCube=[[8,1,6],[3,5,7],[4,9,2]]
    allPoMcs.append(magicCube)
    rfCube=[[8,1,6],[3,5,7],[4,9,2]]
    reflectCube(rfCube)
    allPoMcs.append(rfCube)
    for i in range(3):
        rotateCube(magicCube)
        allPoMcs.append(magicCube)
        rotateCube(rfCube)
        allPoMcs.append(rfCube)
    
    return allPoMcs

def formingMagicSquare(s):

    magicCube=allMagicCube()

    cost=[]

    s=np.array(s)


    for i in magicCube:
        cost.append(np.abs(np.sum(s-np.array(i))))

    return min(cost)


print(formingMagicSquare([[4,9,2],[3,5,7],[8,1,5]]))
print(formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))

