import copy as cp

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

## function to reflect matrix along y-axis

def reflectCube(A):
    for i in range(3):
        hold = A[i][0]
        A[i][0]=A[i][-1]
        A[i][-1]=hold


def allMagicCube():
    allPoMcs=[]
    magicCube=[[8,1,6],[3,5,7],[4,9,2]]
    allPoMcs.append(cp.deepcopy(magicCube))
    rfCube=cp.deepcopy(magicCube)
    reflectCube(rfCube)
    allPoMcs.append(cp.deepcopy(rfCube))
    for i in range(3):
        rotateCube(magicCube)
        allPoMcs.append(cp.deepcopy(magicCube))
        rotateCube(rfCube)
        allPoMcs.append(cp.deepcopy(rfCube))
    
    return allPoMcs

def formingMagicSquare(s):

    magicCube=allMagicCube()

    cost=[]



    for i in magicCube:
        initCost=0
        for j in range(len(i[0])):

            for k in range(len(i[0])):

                initCost += abs(s[j][k]-i[j][k])

        cost.append(abs(initCost))


    return min(cost)



###     ---------------      TEST CASES      ----------------       ###


print(formingMagicSquare([[4,9,2],[3,5,7],[8,1,5]]))
print(formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))
print(formingMagicSquare([[4,8,2],[4,5,7],[6,1,6]]))

