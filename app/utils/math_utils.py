def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Menggunakan Extended Euclidean Algorithm
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        
        x2, x1 = x1, x
        d, y1 = y1, y
        
    if temp_phi == 1:
        return d + phi if d < 0 else d
    return None