from lista_circular_doble import List
from polinomio import Polinomio

primer_poli = List()
segundo_poli = List()


# El codigo puede añadir polinomios en cualquier posicion no importa el grado que desee

def main():
    while True:
        print('Bien que haremos con los polinomio')
        print('Seleccione 1 si quiere agregar algo al polinomio: ')
        print('Seleccione 2 si quiere quitar algo al polinomio: ')
        print('Seleccione 4 si ver una lista: ')
        opciones = int(input('¿Que es lo que haremos?: '))

        if opciones == 1:
            print('Seleccione a o b para decidir que polinomio creara')
            polinomio = input()

            if polinomio == 'a':
                signo = input('Ingrese el signo: ')
                coeficiente = int(input('Ingrese el coeficiente: '))
                grado = int(input('Ingrese el grado: '))
                a = Polinomio(signo, coeficiente, grado)
                buscar = grado - 1
                segundo_poli.search_data(buscar)
                primer_poli.prepend(a)

            if polinomio == 'b':
                signo = input('Ingrese la variable: ')
                coeficiente = int(input('Ingrese el coeficiente: '))
                grado = int(input('Ingrese el grado: '))
                b = Polinomio(signo, coeficiente, grado)
                buscar = grado - 1
                segundo_poli.search_data(buscar)
                primer_poli.prepend(b)

        if opciones == 2:
            print('Seleccione ´a´ o ´b´ para decidir que polinomio creara')
            polinomio = input()

            if polinomio == 'a':
                grado = int(input('Ingrese el grado: '))
                primer_poli.eliminar(grado)

            if polinomio == 'b':
                grado = int(input('Ingrese el grado: '))
                segundo_poli.eliminar(grado)

        if opciones == 4:
            print('Seleccione ´a´ para ver el pimer polinomio y ´b´ para el segundo')
            ver_lista = input('¿Que lista desea ver?: ')

            if ver_lista == 'a':
                print(primer_poli.transversal())

            if ver_lista == 'b':
                print(segundo_poli.transversal())


main()
