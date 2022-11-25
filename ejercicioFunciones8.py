def suma(listaNumeros):
    for numero in listaNumeros: 
     print(numero)
    if numero==listaNumeros[0]:
     print(numero)
    suma(listaNumeros[0 + 1])
   

listaNumeros = [1, 2, 3, 4]
suma(listaNumeros)