#Tower of hanoi
def Hanoi(n, A, B, C):
    if n==1:
        print("Move Ring 1 from Rod", A)
        return
    Hanoi(n-1, A, B, C)
    print("Move ring ", n, "from Rod", A, " to Rod", C)
    Hanoi(n-1, B, C, A)
Hanoi(3, 'A', 'B', 'C')