class Polinomio:
    def __init__(self, signo: str, coeficiente: int, grado: int):
        self.signo = signo
        self.coeficiente = coeficiente
        self.variable = 'x'
        self.grado = grado

    def __str__(self):
        return f'{self.signo}{self.coeficiente}{self.variable}^{self.grado}'