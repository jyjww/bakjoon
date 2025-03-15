
def is_prime(a):
    if (a<2):
        return False
    for i in range(2,a):
        if (a%i == 0):
            return False
    return True
a = int(input())

for i in range(a):
    b= int(input())
    half = b // 2
    A, B = half, half
    for j in range (half):
        if is_prime(A) and is_prime(B):
            print(A, B)
            break
        else :
            A -= 1
            B += 1