import math

PI = 3.14

class Formule(object):
    def perioada(self, Omega): #T
        T = (2*PI)/Omega
        print("Perioada este {0:.2f} secunde/a".format(T))

    def frecventa(self, Omega): #Fr
        Fr = Omega/(2*PI)
        print("Frecventa este {0:.2f} Hz".format(Fr))

    def elongatia(self, A, Omega, Phi0, t): #y
        y = A * math.sin(Omega * t + Phi0)
        print("Elongatia la momentul t={} secunde/secunda este: {} metri".format(t, y))
        print("Legea miscarii este: y = {}sin({}t + {})".format(A, Omega, Phi0))

    def acceleratia(self, A, Omega, Phi0, t): #a
        a = (-Omega*-Omega)*A*math.cos(Omega * t + Phi0)
        print("Acceleratia este: {0:.2f} metri/s2".format(a))

    def acceleratia_max(self, Omega, A): #Amax
        Amax = (-Omega*-Omega) * A
        print("Acceleratia maxima este: {0:.2f} metri/s2".format(Amax))

    def viteza(self, A, Omega, Phi0, t): #v
        v = Omega*A*math.cos(Omega * t + Phi0)
        print("Viteza este: {0:.2f} metri/s".format(v))
        print("Legea vitezei este: v = {}*{}sin({}t + {})".format(Omega, A, Omega, Phi0))

    def viteza_max(self, Omega, A): #Vmax
        Vmax = Omega * A
        print("Viteza maxima este: {0:.2f} metri/s".format(Vmax))

    def pulsatieT(self, T): #Omega
        Omega = 6.28/T
        print("Pulsatia este: {0:.2f} rad/s".format(Omega))

    def pulsatieF(self, Fr):
        Omega = 6.28*Fr
        print("Pulsatia este: {0:.2f} rad/s".format(Omega))

if __name__ == "__main__":
    Formula = Formule()
    alegere = int(input(("Ce vrei sa afli?: \n1. Perioada \n2. Frecventa \n3. Legea miscarii \n4. Acceleratia \n5. Acceleratia Maxima \n6. Viteza \n7. Viteza Maxima \n8. Pulsatia \n")))
    if alegere == 1:
        Omega = float(input("Pulsatia: "))
        Formula.perioada(Omega)
    if alegere == 2:
        Omega = float(input("Pulsatia: "))
        Formula.frecventa(Omega)
    if alegere == 3:
        A = float(input("Amplitudinea: "))
        Omega = float(input("Pulsatia: "))
        Phi0 = float(input("Faza initiala: "))
        t = float(input("Momentul t (Vom afla si elongatia unui moment tot odata): "))
        Formula.elongatia(A, Omega, Phi0, t)
    if alegere == 4:
        A = float(input("Amplitudinea: "))
        Omega = float(input("Pulsatia: "))
        Phi0 = float(input("Faza initiala: "))
        t = float(input("Momentul t: "))
        Formula.acceleratia(A, Omega, Phi0, t)
    if alegere == 5:
        A = float(input("Amplitudinea: "))
        Omega = float(input("Pulsatia: "))
        Formula.acceleratia_max(Omega, A)
    if alegere == 6:
        A = float(input("Amplitudinea: "))
        Omega = float(input("Pulsatia: "))
        Phi0 = float(input("Faza initiala: "))
        t = float(input("Momentul t: "))
        Formula.viteza(A, Omega, Phi0, t)
    if alegere == 7:
        A = float(input("Amplitudinea: "))
        Omega = float(input("Pulsatia: "))
        Formula.viteza_max(Omega, A)
    if alegere == 8:
        PsauF = input("Doresti sa afli pulsatia din Perioada sau din Frecventa? P pentru Pulsatie sau F pentru Frecventa: ")
        if(PsauF == "P"):
            T = float(input("Perioada: "))
            Formula.pulsatieT(T)
        if(PsauF == "F"):
            Fr = float(input("Frecventa: "))
            Formula.pulsatieF(Fr)
