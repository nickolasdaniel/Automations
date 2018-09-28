#include <iostream>
#include <string.h>
using namespace std;
//This could have been easily done without OOP, but I'm learning so it is a great exercise :)
//Class for matrix functions;
class Operatii {
  public:
    void adunare_matrice(int a[10][10], int b[10][10], int c[10][10], int n) {
      int i, j;
      for(i=1; i<=n; i++) {
        for(j=1; j<=n; j++) {
          c[i][j] = a[i][j] + b[i][j];
        }
      }
    }

    void inmultire_matrice(int a[10][10], int b[10][10], int c[10][10], int n) {
      int i, j;
      for(i=1; i<=n; i++) {
        for(j=1; j<=n; j++) {
          c[i][j] = a[i][j] * b[i][j];
        }
      }
    }

    void patrat_matrice(int a[10][10], int c[10][10], int n) {
      int i, j;
      for(i=1; i<=n; i++) {
        for(j=1; j<=n; j++) {
          c[i][j] = a[i][j] * a[i][j];
        }
      }
    }

    int urma_matrice(int a[10][10], int n) {
      int i, urma = 0;
      for(i=1; i<=n; i++) {
          urma += a[i][i];
      }
      return urma;
    }
};

//Class for reading/writing matrix;
class Standard {
  public:
    void citire_matrice(int a[10][10], int n) {
      int i, j;
      for(i=1; i<=n; i++) {
        for(j=1; j<=n; j++) {
          cout<<"a["<<i<<"]["<<j<<"] = "; cin>>a[i][j];
        }
      }
    }
    void afisare_matrice(int a[10][10], int n) {
      int i, j;
      for(i=1; i<=n; i++) {
        for(j=1; j<=n; j++) {
          cout<<a[i][j]<<" ";
        }
        cout<<endl;
      }
    }
};

int main() {
  int a[10][10], b[10][10], c[10][10], n, i, j;
  Operatii matriceO;
  Standard matriceS;
  int varianta1, varianta2, varianta3;
  cout<<"Pentru a efectua operatii cu matrici apasati 0, pentru urma matricii apasati 1: "; cin>>varianta1;
  if(varianta1 == 0) {
      cout<<"Vrei sa ridici la patrat o matrice? 0 - Da, 1 - Nu: "; cin>>varianta2;
      if(varianta2 == 0) {
        cout<<"Dimensiunea matricei: "; cin>>n;
        matriceS.citire_matrice(a, n);
        matriceO.patrat_matrice(a, c, n);
        matriceS.afisare_matrice(c, n);
      } else if(varianta2 == 1) {
          cout<<"Dimensiunea matricelor: "; cin>>n;
          cout<<"Prima matrice: "<<endl;
            matriceS.citire_matrice(a, n);
            matriceS.afisare_matrice(a, n);
          cout<<"A doua matrice: "<<endl;
            matriceS.citire_matrice(b, n);
            matriceS.afisare_matrice(a, n);
          cout<<"Tasteaza 0 pentru a aduna, sau 1 pentru a inmulti matricile: "; cin>>varianta3;
          if(varianta3 == 0) {
            matriceO.adunare_matrice(a, b, c, n);
            matriceS.afisare_matrice(c, n);
          } else if (varianta3 == 1) {
            matriceO.inmultire_matrice(a, b, c, n);
            matriceS.afisare_matrice(c, n);
          }
      }
} else if(varianta1 == 1) {
        cout<<"Dimensiunea matricei: "; cin>>n;
        matriceS.citire_matrice(a, n);
        matriceS.afisare_matrice(a, n);
        cout<<"Urma acestei matrice este: "<<matriceO.urma_matrice(a, n);
    }
}



