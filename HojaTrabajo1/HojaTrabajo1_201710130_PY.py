print("---HOJA DE TRABAJO 1--- ")
print("EJERCICIO 1: TRIÁNGULO ")
print()
print("Ingrese un valor entero positivo: ")
triangulo = int(input())
for i in range (triangulo):
    print('*' *(i+1) )
print("EJERCICIO 2: NÚMERO PRIMO ")
print("Ingrese un número entero ")
primo = int(input())
for i in range(2, primo):
    if primo % i == 0:
        break
if (1+i) == primo :
    print(str(primo) + " Es primo ")
else:
    print(str(primo) + " No es primo ")

