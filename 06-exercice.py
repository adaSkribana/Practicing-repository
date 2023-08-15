class Calculator:
    def __init__(self, n1, n2):
        self.sum = n1 + n2
        self.rest = n1 - n2
        self.multiplication = n1 * n2
        self.division = n1 / n2
operation = Calculator(n1= int(input("Ingresa el primer valor: ")), n2= int(input("ingresa el segundo valor: ")))
print(operation.multiplication)

#como integraria un menu para escoger la operacion a realizar ¿?

