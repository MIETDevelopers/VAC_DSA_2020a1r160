n=4
m = [
    [1,1,1,1],
    [1,1,1,1],
    [1,0,1,1],
    [1,1,1,1]
]

def getCount(m,n):
    lst0 = [0 for i in range(4)]
    lst1 = [0 for i in range(4)]
    left = True
    right = True
    left1 = True
    right1 = True
    for i in range(n):
        if m[i].count(0) == n:
            lst0[0] +=1
        if m[i].count(1) == n:
            lst1[0] +=1
        horizontalState = True
        horizontalState1 = True
        for j in range(n):
            if m[j][i] != 0:
                horizontalState = False
            if j == i and m[i][j] !=0:
                left = False
            if j == n-i-1 and m[i][j] != 0:
                right = False
            if m[j][i] != 1:
                horizontalState1 = False
            if j == i and m[i][j] !=1:
                left1 = False
            if j == n-i-1 and m[i][j] != 1:
                right1 = False
        if horizontalState == True:
            lst0[1] +=1
        if horizontalState1 == True:
            lst1[1] +=1
    if left == True:
        lst0[2]=1
    if right == True:
        lst0[3]=1
    if left1 == True:
        lst1[2]=1
    if right1 == True:
        lst1[3]=1
    return [lst0,lst1]
print(getCount(m,n))