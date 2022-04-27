A = 2
B = 7
C = 3.5
L = False

ex_a = True and True

print("Ex a: ", ex_a)

ex_b = True and L
print("Ex b: ", ex_b)

ex_c = True or L
print("Ex c: ", ex_c)

ex_d = False or 20//3 != 2
print("Ex d: ", ex_d)

ex_e = L or A % B > C
print("Ex e: ", ex_e)

ex_f = B == A * C and (L or True)
print("Ex f: ", ex_f)

ex_g = B / A == C or B / A != C
print("Ex g: ", ex_g)

ex_h = B > A or B == A ** A
print("Ex h: ", ex_h)

ex_i = L and B // A >= C or not A <= C
print("Ex i: ", ex_i)

ex_j = not L or True and (A + B)**0.5 >= C
print("Ex j: ", ex_j)

ex_k = not L or 3**2 / 3 < 15 - 35 % 7
print("Ex k: ", ex_k)

ex_l = not (5 != 10 / 2) or True and 2 - 5 > 5-2
print("Ex l: ", ex_l)

ex_m = L or B**A <= C * 10 + A * B
print("Ex m: ", ex_m)