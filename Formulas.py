from sympy import *


# 1. Defined symbols
G,rho,r1,r2,r,theta1,theta2,lam1,lam2,lam = symbols('G rho r1 r2 r theta1 theta2 lam1 lam2 lam')


# 2. Expressions in Table 8
A22 = 4 * r2**2 + r**2 * (1 - 3 * cos(2*theta2)) - 2 * r * r2 * cos(theta2)
A12 = 4 * r1**2 + r**2 * (1 - 3 * cos(2*theta2)) - 2 * r * r1 * cos(theta2)
A21 = 4 * r2**2 + r**2 * (1 - 3 * cos(2*theta1)) - 2 * r * r2 * cos(theta1)
A11 = 4 * r1**2 + r**2 * (1 - 3 * cos(2*theta1)) - 2 * r * r1 * cos(theta1)
B2 = r**3 * (sin(theta2))**2 * cos(theta2)
B1 = r**3 * (sin(theta1))**2 * cos(theta1)
C22 = r2 - r * cos(theta2)
C12 = r1 - r * cos(theta2)
C21 = r2 - r * cos(theta1)
C11 = r1 - r * cos(theta1)
l22 = (r**2 + r2**2 - 2 * r * r2 * cos(theta2))**0.5
l12 = (r**2 + r1**2 - 2 * r * r1 * cos(theta2))**0.5
l21 = (r**2 + r2**2 - 2 * r * r2 * cos(theta1))**0.5
l11 = (r**2 + r1**2 - 2 * r * r1 * cos(theta1))**0.5


# 3. Expressions in Table 9
D22 = r2**2 + r**2 * (3 * (cos(theta2))**2 - 2) + r * r2 * cos(theta2)
D12 = r1**2 + r**2 * (3 * (cos(theta2))**2 - 2) + r * r1 * cos(theta2)
D21 = r2**2 + r**2 * (3 * (cos(theta1))**2 - 2) + r * r2 * cos(theta1)
D11 = r1**2 + r**2 * (3 * (cos(theta1))**2 - 2) + r * r1 * cos(theta1)


# 4. Expressions in Table 10
E22 = r**4 + r**2 * r2**2 + 4 * r2**4 - r * r2 * (r**2 + 4 * r2**2) * cos(theta2) \
        - r**2 * (3 * r**2 + r2**2) * cos(2*theta2) + 3 * r**3 * r2 * cos(3*theta2)
E12 = r**4 + r**2 * r1**2 + 4 * r1**4 - r * r1 * (r**2 + 4 * r1**2) * cos(theta2) \
        - r**2 * (3 * r**2 + r1**2) * cos(2*theta2) + 3 * r**3 * r1 * cos(3*theta2)
E21 = r**4 + r**2 * r2**2 + 4 * r2**4 - r * r2 * (r**2 + 4 * r2**2) * cos(theta1) \
        - r**2 * (3 * r**2 + r2**2) * cos(2*theta1) + 3 * r**3 * r2 * cos(3*theta1)
E11 = r**4 + r**2 * r1**2 + 4 * r1**4 - r * r1 * (r**2 + 4 * r1**2) * cos(theta1) \
        - r**2 * (3 * r**2 + r1**2) * cos(2*theta1) + 3 * r**3 * r1 * cos(3*theta1)


# 5. Expressions in Table 11
F2 = - 3 * cos(theta2) * (8 * (lam2 - lam1) * (sin(theta2))**2 \
        + 4 * cos(2*lam-lam1-lam2) * sin(lam2 - lam1)*(5-cos(2*theta2)))
F1 = - 3 * cos(theta1) * (8 * (lam2 - lam1) * (sin(theta1))**2 \
        + 4 * cos(2*lam-lam1-lam2) * sin(lam2 - lam1)*(5-cos(2*theta1)))
H2 = - 4 * (r**4 + r**2 * r2**2 + 4 * r2**4) * (lam2 - lam1)
H1 = - 4 * (r**4 + r**2 * r1**2 + 4 * r1**4) * (lam2 - lam1)
I22 = 2 * r**2 * ((3 * r**2 + r2**2)*cos(2*theta2) - 3 * r * r2 * cos(3*theta2)) * \
        (2*lam2 - 2*lam1 + sin(2*(lam-lam1)) - sin(2*(lam-lam2)))
I12 = 2 * r**2 * ((3 * r**2 + r1**2)*cos(2*theta2) - 3 * r * r1 * cos(3*theta2)) * \
        (2*lam2 - 2*lam1 + sin(2*(lam-lam1)) - sin(2*(lam-lam2)))
I21 = 2 * r**2 * ((3 * r**2 + r2**2)*cos(2*theta1) - 3 * r * r2 * cos(3*theta1)) * \
        (2*lam2 - 2*lam1 + sin(2*(lam-lam1)) - sin(2*(lam-lam2)))
I11 = 2 * r**2 * ((3 * r**2 + r1**2)*cos(2*theta1) - 3 * r * r1 * cos(3*theta1)) * \
        (2*lam2 - 2*lam1 + sin(2*(lam-lam1)) - sin(2*(lam-lam2)))
J2 = - 4 * (13 * r**4 + 13 * r**2 * r2**2 + 4 * r2**4) * \
        cos(2*lam - lam1 - lam2) * sin(lam2 - lam1)
J1 = - 4 * (13 * r**4 + 13 * r**2 * r1**2 + 4 * r1**4) * \
        cos(2*lam - lam1 - lam2) * sin(lam2 - lam1)
K22 = 4 * r * r2 * cos(theta2) * ((r**2 + 4 * r2**2) * (lam2 - lam1) + \
        (25 * r**2 + 4 * r2**2)* cos(2 * lam - lam1 -lam2) * sin(lam2 - lam1))
K12 = 4 * r * r1 * cos(theta2) * ((r**2 + 4 * r1**2) * (lam2 - lam1) + \
        (25 * r**2 + 4 * r1**2)* cos(2 * lam - lam1 -lam2) * sin(lam2 - lam1))
K21 = 4 * r * r2 * cos(theta1) * ((r**2 + 4 * r2**2) * (lam2 - lam1) + \
        (25 * r**2 + 4 * r2**2)* cos(2 * lam - lam1 -lam2) * sin(lam2 - lam1))
K11 = 4 * r * r1 * cos(theta1) * ((r**2 + 4 * r1**2) * (lam2 - lam1) + \
        (25 * r**2 + 4 * r1**2)* cos(2 * lam - lam1 -lam2) * sin(lam2 - lam1))


# 6. Expressions in Table 12
L2 = - 3 * cos(theta2) * (8 * (lam2 - lam1)* (sin(theta2))**2 \
        - 4 * cos(2*lam - lam1 -lam2) * sin(lam2 - lam1) * (5 - cos(2*theta2)))
L1 = - 3 * cos(theta1) * (8 * (lam2 - lam1)* (sin(theta1))**2 \
        - 4 * cos(2*lam - lam1 -lam2) * sin(lam2 - lam1) * (5 - cos(2*theta1)))
M22 = 2 * r**2 * ((3 * r**2 + r2**2) * cos(2*theta2) - 3 * r * r2 * cos(3 * theta2)) * \
        (2 * lam2 - 2 * lam1 - sin(2*(lam-lam1)) + sin(2*(lam-lam2)))
M12 = 2 * r**2 * ((3 * r**2 + r1**2) * cos(2*theta2) - 3 * r * r1 * cos(3 * theta2)) * \
        (2 * lam2 - 2 * lam1 - sin(2*(lam-lam1)) + sin(2*(lam-lam2)))
M21 = 2 * r**2 * ((3 * r**2 + r2**2) * cos(2*theta1) - 3 * r * r2 * cos(3 * theta1)) * \
        (2 * lam2 - 2 * lam1 - sin(2*(lam-lam1)) + sin(2*(lam-lam2)))
M11 = 2 * r**2 * ((3 * r**2 + r1**2) * cos(2*theta1) - 3 * r * r1 * cos(3 * theta1)) * \
        (2 * lam2 - 2 * lam1 - sin(2*(lam-lam1)) + sin(2*(lam-lam2)))
N22 = 4 * r * r2 * cos(theta2) * ((r**2 + 4 * r2**2) * (lam2 - lam1) \
        - (25 * r**2 + 4 * r2**2) * cos(2*lam - lam1 - lam2) * sin(lam2 - lam1))
N12 = 4 * r * r1 * cos(theta2) * ((r**2 + 4 * r1**2) * (lam2 - lam1) \
        - (25 * r**2 + 4 * r1**2) * cos(2*lam - lam1 - lam2) * sin(lam2 - lam1))
N21 = 4 * r * r2 * cos(theta1) * ((r**2 + 4 * r2**2) * (lam2 - lam1) \
        - (25 * r**2 + 4 * r2**2) * cos(2*lam - lam1 - lam2) * sin(lam2 - lam1))
N11 = 4 * r * r1 * cos(theta1) * ((r**2 + 4 * r1**2) * (lam2 - lam1) \
        - (25 * r**2 + 4 * r1**2) * cos(2*lam - lam1 - lam2) * sin(lam2 - lam1))


# 7. Expressions in Table 13
O22 = r2**3 * (9 * r**2 * r2 + 4 * r2**3 - 4 * r * (r**2 + 3 * r2**2) * cos(theta2) + \
        3 * r**2 * r2 * cos(2*theta2))
O12 = r1**3 * (9 * r**2 * r1 + 4 * r1**3 - 4 * r * (r**2 + 3 * r1**2) * cos(theta2) + \
        3 * r**2 * r1 * cos(2*theta2))
O21 = r2**3 * (9 * r**2 * r2 + 4 * r2**3 - 4 * r * (r**2 + 3 * r2**2) * cos(theta1) + \
        3 * r**2 * r2 * cos(2*theta1))
O11 = r1**3 * (9 * r**2 * r1 + 4 * r1**3 - 4 * r * (r**2 + 3 * r1**2) * cos(theta1) + \
        3 * r**2 * r1 * cos(2*theta1))


# 8. Expressions in Table 14
P22 = 6*r**2 * r2**4 * cos(2*theta2) * (2*lam2 - 2*lam1 + sin(2*(lam-lam1)) - sin(2*(lam-lam2)))
P12 = 6*r**2 * r1**4 * cos(2*theta2) * (2*lam2 - 2*lam1 + sin(2*(lam-lam1)) - sin(2*(lam-lam2)))
P21 = 6*r**2 * r2**4 * cos(2*theta1) * (2*lam2 - 2*lam1 + sin(2*(lam-lam1)) - sin(2*(lam-lam2)))
P11 = 6*r**2 * r1**4 * cos(2*theta1) * (2*lam2 - 2*lam1 + sin(2*(lam-lam1)) - sin(2*(lam-lam2)))
U22 = (1 - (2*r*r2*cos(theta2))/(r**2+r2**2))**0.5
U12 = (1 - (2*r*r1*cos(theta2))/(r**2+r1**2))**0.5
U21 = (1 - (2*r*r2*cos(theta1))/(r**2+r2**2))**0.5
U11 = (1 - (2*r*r1*cos(theta1))/(r**2+r1**2))**0.5
Q22 = -cos(2*lam-lam1-lam2) * sin(lam2-lam1) * (5 * r**6 * U22 + \
        r2**6 * (5*U22 -16) + r**2 * r2**4 * (15*U22 - 52) + r**4 * r2**2 * (15*U22 -16))
Q12 = -cos(2*lam-lam1-lam2) * sin(lam2-lam1) * (5 * r**6 * U12 + \
        r1**6 * (5*U12 -16) + r**2 * r1**4 * (15*U12 - 52) + r**4 * r1**2 * (15*U12 -16))
Q21 = -cos(2*lam-lam1-lam2) * sin(lam2-lam1) * (5 * r**6 * U21 + \
        r2**6 * (5*U21 -16) + r**2 * r2**4 * (15*U21 - 52) + r**4 * r2**2 * (15*U21 -16))
Q11 = -cos(2*lam-lam1-lam2) * sin(lam2-lam1) * (5 * r**6 * U11 + \
        r1**6 * (5*U11 -16) + r**2 * r1**4 * (15*U11 - 52) + r**4 * r1**2 * (15*U11 -16))
R22 = 2 * r * r2 * cos(theta2) * ((lam2-lam1)*(5 * r**4 * U22 + r2**4 *(5*U22 - 24) + \
        2 * r**2 * r2**2 * (5*U22-4)) + (r**2 + r2**2) * (5 * r**2 * U22 + \
        r2**2 * (5*U22 - 24)) * cos(2*lam - lam1 -lam2) * sin(lam2 -lam1))
R12 = 2 * r * r1 * cos(theta2) * ((lam2-lam1)*(5 * r**4 * U12 + r1**4 *(5*U12 - 24) + \
        2 * r**2 * r1**2 * (5*U12-4)) + (r**2 + r1**2) * (5 * r**2 * U12 + \
        r1**2 * (5*U12 - 24)) * cos(2*lam - lam1 -lam2) * sin(lam2 -lam1))
R21 = 2 * r * r2 * cos(theta2) * ((lam2-lam1)*(5 * r**4 * U21 + r2**4 *(5*U21 - 24) + \
        2 * r**2 * r2**2 * (5*U21-4)) + (r**2 + r2**2) * (5 * r**2 * U21 + \
        r2**2 * (5*U21 - 24)) * cos(2*lam - lam1 -lam2) * sin(lam2 -lam1))
R11 = 2 * r * r1 * cos(theta2) * ((lam2-lam1)*(5 * r**4 * U11 + r1**4 *(5*U11 - 24) + \
        2 * r**2 * r1**2 * (5*U11-4)) + (r**2 + r1**2) * (5 * r**2 * U11 + \
        r1**2 * (5*U11 - 24)) * cos(2*lam - lam1 -lam2) * sin(lam2 -lam1))
S22 = - 5 * (r**2 + r2**2)**3 * (lam2-lam1) * U22
S12 = - 5 * (r**2 + r1**2)**3 * (lam2-lam1) * U12
S21 = - 5 * (r**2 + r2**2)**3 * (lam2-lam1) * U21
S11 = - 5 * (r**2 + r1**2)**3 * (lam2-lam1) * U11
T2 = 4 * r2**4 * (9 * r**2 + 4 * r2**2) * (lam2-lam1)
T1 = 4 * r1**4 * (9 * r**2 + 4 * r1**2) * (lam2-lam1)


# 9. Expressions in Table 15
V22 = 6 * r**2 * r2**4 *cos(2*theta2) *(2*lam2 -2*lam1 -sin(2*(lam-lam1)) + sin(2*(lam-lam2)))
V12 = 6 * r**2 * r1**4 *cos(2*theta2) *(2*lam2 -2*lam1 -sin(2*(lam-lam1)) + sin(2*(lam-lam2)))
V21 = 6 * r**2 * r2**4 *cos(2*theta1) *(2*lam2 -2*lam1 -sin(2*(lam-lam1)) + sin(2*(lam-lam2)))
V11 = 6 * r**2 * r1**4 *cos(2*theta1) *(2*lam2 -2*lam1 -sin(2*(lam-lam1)) + sin(2*(lam-lam2)))
W22 = 2 * r * r2 * cos(theta2) * ((lam2-lam1) * (5 * r**4 * U22 + r2**4 * (5 * U22 - 24) +\
        + 2 * r**2 * r2**2 * (5 * U22 - 4)) - (r**2 + r2**2) * (5 * r**2 * U22 +\
        r2**2 * (5 * U22 -24)) * cos(2 * lam - lam1 - lam2) * sin(lam2 - lam1))
W12 = 2 * r * r1 * cos(theta2) * ((lam2-lam1) * (5 * r**4 * U12 + r1**4 * (5 * U12 - 24) +\
        + 2 * r**2 * r1**2 * (5 * U12 - 4)) - (r**2 + r1**2) * (5 * r**2 * U12 +\
        r1**2 * (5 * U12 -24)) * cos(2 * lam - lam1 - lam2) * sin(lam2 - lam1))
W21 = 2 * r * r2 * cos(theta1) * ((lam2-lam1) * (5 * r**4 * U21 + r2**4 * (5 * U21 - 24) +\
        + 2 * r**2 * r2**2 * (5 * U21 - 4)) - (r**2 + r2**2) * (5 * r**2 * U21 +\
        r2**2 * (5 * U21 -24)) * cos(2 * lam - lam1 - lam2) * sin(lam2 - lam1))
W11 = 2 * r * r1 * cos(theta1) * ((lam2-lam1) * (5 * r**4 * U11 + r1**4 * (5 * U11 - 24) +\
        + 2 * r**2 * r1**2 * (5 * U11 - 4)) - (r**2 + r1**2) * (5 * r**2 * U11 +\
        r1**2 * (5 * U11 -24)) * cos(2 * lam - lam1 - lam2) * sin(lam2 - lam1))


# 10. Expressions in Table 16
X22 = 4 * r2**4 * (9 * r**2 + 4 * r2**2 + 3 * r**2 * cos(2*theta2))
X12 = 4 * r1**4 * (9 * r**2 + 4 * r1**2 + 3 * r**2 * cos(2*theta2))
X21 = 4 * r2**4 * (9 * r**2 + 4 * r2**2 + 3 * r**2 * cos(2*theta1))
X11 = 4 * r1**4 * (9 * r**2 + 4 * r1**2 + 3 * r**2 * cos(2*theta1))
Y22 = 2 * r * r2 * cos(theta2) * (5 * r**4 * U22 + r2**4 * (5 * U22 - 24) + \
        2 * r**2 * r2**2 * (5 * U22 - 4))
Y12 = 2 * r * r1 * cos(theta2) * (5 * r**4 * U12 + r1**4 * (5 * U12 - 24) + \
        2 * r**2 * r1**2 * (5 * U12 - 4))
Y21 = 2 * r * r2 * cos(theta1) * (5 * r**4 * U21 + r2**4 * (5 * U21 - 24) + \
        2 * r**2 * r2**2 * (5 * U21 - 4))
Y11 = 2 * r * r1 * cos(theta1) * (5 * r**4 * U11 + r1**4 * (5 * U11 - 24) + \
        2 * r**2 * r1**2 * (5 * U11 - 4))
Z22 = - 5 * (r**2 + r2**2)**3 * U22
Z12 = - 5 * (r**2 + r1**2)**3 * U12
Z21 = - 5 * (r**2 + r2**2)**3 * U21
Z11 = - 5 * (r**2 + r1**2)**3 * U11


# 11. Analytical formula of the GP of a tesseroid in Sect. 2.1
# Eq. (4)
V = G * rho * (lam2 - lam1) / (12*r) * (A22*l22 - A12*l12 - A21*l21 + A11*l11 + \
        6 * B2 * log((C22+l22)/(C12+l12)) + 6 * B1* log((C11+l11)/(C21+l21)))
print("\nAnalytical formula of the GP (V) of a tesseroid in Sect. 2.1 is",V)


# 12. Analytical formula of the radial GV of a tesseroid in Sect. 2.2
# Eq. (7)
Vr = - G * rho * (lam2 - lam1) / (3 * r**2) * (D22*l22 - D12*l12 - D21*l21 + D11*l11 + \
        3 * B2 * log((C12+l12)/(C22+l22)) + 3 * B1 * log((C21+l21)/(C11+l11)))
print("\nAnalytical formula of the radial GV (Vr) of a tesseroid in Sect. 2.2 is",Vr)


# 13. Analytical formulas of the GGT of a tesseroid in Sect. 2.3
# Eq. (9)
Vzz = G * rho * (lam2 - lam1)/(6 * r**3) * (E22/l22 - E12/l12 - E21/l21 + E11/l11 + \
        6 * B2 * log((C22+l22)/(C12+l12)) + 6 * B1* log((C11+l11)/(C21+l21)))
print("\nAnalytical formula of the GGT (Vzz) of a tesseroid in Sect. 2.3 is",Vzz)

# Eq. (14)
Vxx = G * rho / 48 * (F2 * log((C22+l22)/(C12+l12)) + F1 * log((C11+l11)/(C21+l21)) + \
        (H2+I22+J2+K22)/(r**3 * l22) - (H1+I12+J1+K12)/(r**3 * l12) - \
        (H2+I21+J2+K21)/(r**3 * l21) + (H1+I11+J1+K11)/(r**3 * l11))
print("\nAnalytical formula of the GGT (Vxx) of a tesseroid in Sect. 2.3 is",Vxx)

# Eq. (15)
Vyy = G * rho / 48 * (L2 * log((C22+l22)/(C12+l12)) + L1 * log((C11+l11)/(C21+l21)) + \
        (H2+M22-J2+N22)/(r**3 * l22) - (H1+M12-J1+N12)/(r**3 * l12) - \
        (H2+M21-J2+N21)/(r**3 * l21) + (H1+M11-J1+N11)/(r**3 * l11))
print("\nAnalytical formula of the GGT (Vyy) of a tesseroid in Sect. 2.3 is",Vyy)


# 14. Analytical formulas of the GC of a tesseroid in Sect. 2.4
# Eq. (17)
Vzzz = - G * rho * (lam2-lam1)/(2 * r**4) * (O22/(l22**3) - \
         O12/(l12**3) - O21/(l21**3) + O11/(l11**3))
print("\nAnalytical formula of the GC (Vzzz) of a tesseroid in Sect. 2.4 is",Vzzz)

# Eq. (20)
Vxxz = G * rho / (16 * r**4) * ((P22+Q22+R22+S22+T2)/(l22**3) - \
                                (P12+Q12+R12+S12+T1)/(l12**3) - \
                                (P21+Q21+R21+S21+T2)/(l21**3) + \
                                (P11+Q11+R11+S11+T1)/(l11**3))
print("\nAnalytical formula of the GC (Vxxz) of a tesseroid in Sect. 2.4 is",Vxxz)

# Eq. (21)
Vyyz = G * rho / (16 * r**4) * ((V22-Q22+W22+S22+T2)/(l22**3) - \
                                (V12-Q12+W12+S12+T1)/(l12**3) - \
                                (V21-Q21+W21+S21+T2)/(l21**3) + \
                                (V11-Q11+W11+S11+T1)/(l11**3))
print("\nAnalytical formula of the GC (Vyyz) of a tesseroid in Sect. 2.4 is",Vyyz)


# 15. Analytical formulas of gravitational effects of a spherical zonal band in Sect. 2.5
# Eq. (22)
SphericalZonalBandV = pi * G * rho / (6 * r) * (A22*l22 - A12*l12 - A21*l21 + A11*l11 + \
                6 * B2 * log((C22+l22)/(C12+l12)) + 6 * B1 * log((C11+l11)/(C21+l21)))
print("\nAnalytical formula of the GP (V) of a spherical zonal band in Sect. 2.5 is",SphericalZonalBandV)

# Eq. (23)
SphericalZonalBandVr = - 2 * pi * G * rho / (3 * r**2) * (D22*l22 - D12*l12 - D21*l21 + D11*l11 + \
                3 * B2 * log((C12+l12)/(C22+l22)) + 3 * B1 * log((C21+l21)/(C11+l11)))
print("\nAnalytical formula of the radial GV (Vr) of a spherical zonal band in Sect. 2.5 is",SphericalZonalBandVr)

# Eq. (24)
SphericalZonalBandVzz = pi * G * rho /(3 * r**3) * (E22/l22 - E12/l12 - E21/l21 + E11/l11 + \
                6 * B2 * log((C22+l22)/(C12+l12)) + 6 * B1 * log((C11+l11)/(C21+l21)))
print("\nAnalytical formula of the GGT (Vzz) of a spherical zonal band in Sect. 2.5 is",SphericalZonalBandVzz)

# Eq. (25)
SphericalZonalBandVxx = - pi * G * rho / (6 * r**3) * (E22/l22 - E12/l12 - E21/l21 + E11/l11 + \
                6 * B2 * log((C22+l22)/(C12+l12)) + 6 * B1 * log((C11+l11)/(C21+l21)))
print("\nAnalytical formula of the GGT (Vxx) of a spherical zonal band in Sect. 2.5 is",SphericalZonalBandVxx)

# Eq. (25)
SphericalZonalBandVyy = - pi * G * rho / (6 * r**3) * (E22/l22 - E12/l12 - E21/l21 + E11/l11 + \
                6 * B2 * log((C22+l22)/(C12+l12)) + 6 * B1 * log((C11+l11)/(C21+l21)))
print("\nAnalytical formula of the GGT (Vyy) of a spherical zonal band in Sect. 2.5 is",SphericalZonalBandVyy)

# Eq. (26)
SphericalZonalBandVzzz = - pi * G * rho / (r**4) * (O22/(l22**3) - O12/(l12**3) - \
                O21/(l21**3) + O11/(l11**3))
print("\nAnalytical formula of the GC (Vzzz) of a spherical zonal band in Sect. 2.5 is",SphericalZonalBandVzzz)

# Eq. (27)
SphericalZonalBandVxxz = pi * G * rho / (8 * r**4) * ((X22+Y22+Z22)/(l22**3) - \
                (X12+Y12+Z12)/(l12**3) - (X21+Y21+Z21)/(l21**3) + (X11+Y11+Z11)/(l11**3))
print("\nAnalytical formula of the GC (Vxxz) of a spherical zonal band in Sect. 2.5 is",SphericalZonalBandVxxz)

# Eq. (27)
SphericalZonalBandVyyz = pi * G * rho / (8 * r**4) * ((X22+Y22+Z22)/(l22**3) -\
                (X12+Y12+Z12)/(l12**3) - (X21+Y21+Z21)/(l21**3) + (X11+Y11+Z11)/(l11**3))
print("\nAnalytical formula of the GC (Vyyz) of a spherical zonal band in Sect. 2.5 is",SphericalZonalBandVyyz)

# 16. Analytical formulas of gravitational effects of a spherical shell in Sect. 2.6
# Eq. (28)
SphericalShellV = 4 * pi * G * rho * (r2**3 - r1**3)/(3 * r)
print("\nAnalytical formula of the GP (V) of a spherical shell in Sect. 2.6 is",SphericalShellV)

# Eq. (29)
SphericalShellVr = - 4 * pi * G * rho * (r2**3 - r1**3)/(3 * r**2)
print("\nAnalytical formula of the radial GV (Vr) of a spherical shell in Sect. 2.6 is",SphericalShellVr)

# Eq. (30)
SphericalShellVzz = 8 * pi * G * rho * (r2**3 - r1**3)/(3 * r**3)
print("\nAnalytical formula of the GGT (Vzz) of a spherical shell in Sect. 2.6 is",SphericalShellVzz)

# Eq. (31)
SphericalShellVxx = - 4 * pi * G * rho * (r2**3 - r1**3)/(3 * r**3)
print("\nAnalytical formula of the GGT (Vxx) of a spherical shell in Sect. 2.6 is",SphericalShellVxx)

# Eq. (31)
SphericalShellVyy = - 4 * pi * G * rho * (r2**3 - r1**3)/(3 * r**3)
print("\nAnalytical formula of the GGT (Vyy) of a spherical shell in Sect. 2.6 is",SphericalShellVyy)

# Eq. (32)
SphericalShellVzzz = - 8 * pi * G * rho * (r2**3 - r1**3)/(r**4)
print("\nAnalytical formula of the GC (Vzzz) of a spherical shell in Sect. 2.6 is",SphericalShellVzzz)

# Eq. (33)
SphericalShellVxxz = 4 * pi * G * rho * (r2**3 - r1**3)/(r**4)
print("\nAnalytical formula of the GC (Vxxz) of a spherical shell in Sect. 2.6 is",SphericalShellVxxz)

# Eq. (33)
SphericalShellVyyz = 4 * pi * G * rho * (r2**3 - r1**3)/(r**4)
print("\nAnalytical formula of the GC (Vyyz) of a spherical shell in Sect. 2.6 is",SphericalShellVyyz)
