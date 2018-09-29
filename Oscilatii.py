import math

# t = 0
# Fr = 0
# Fo = 0
# T = 0
# Omega = 0
# Phi = 0
# y = 0
# A = 0
# PI = 3.14

class Formule(object):
    def perioada(Omega):
        T = (2*PI)/Omega
        print(T)

    def frecventa():
        pass

    def legea_miscarii(t):
        pass

    def acceleratia(t):
        pass

    def acceleratia_max(t):
        pass

    def viteza(t):
        pass

    def viteza_max(t):
        pass

    def pulsatie():
        pass

if __name__ == "__main__":
    Formula = Formule()
    alegere = input(("Ce vrei sa afli?: \n1. Perioada \n2. Frecventa \n3. Legea miscarii \n4. Acceleratia \n5. Acceleratia Maxima \n6. Viteza \n7. Viteza Maxima \n8. Pulsatia \n"))
    if alegere == 1:
        Omega = int(input("Omega: "))
        print(Omega)
        Formula.perioada(Omega)
