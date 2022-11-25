salario = int(input("por favor ingrese salario"))

def calcularSalario(int:salario):
    " salario =300"
    global salario
    seguro= 50
    salarioTotal = salario - seguro
    return salarioTotal

print(calcularSalario(salario))