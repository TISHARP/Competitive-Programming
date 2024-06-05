def anti_hash_hack(n, x=1, cpython=False):
    """
    Input: integer n > 0
    Output: List A of length n 
    such that x <= A[i] <= x + 2**(n.bit_length() + 2)
    """
    pow2 = 2**(n.bit_length() + 2)
    
    A = [x + pow2]
    i = perturb = x
    while len(A) < n//2:
        A.append(i + pow2)
        if cpython:
            perturb >>= 5
        i = (5 * i + perturb + 1) % pow2
        if not cpython:
            perturb >>= 5
    
    while len(A) < n:
        A.append(x)
    
    return A

n = 200000
A = anti_hash_hack(n, 3, False)
print(1)
print(n)
print(*[i+1 for i in A])
print(*A)
print(n)
print(*A)