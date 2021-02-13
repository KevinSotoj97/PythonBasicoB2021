print('--- Ejercicio 1:  ---')
print('Ingrese su contraseña: ')
ent = str(input())
contra = ent.lower()
validacion = "contraseña"
if contra ==validacion:
    print("Contraseña Válida")
else:
    print("Contrasaña Inválida")

print()
print('--- Ejercicio 2:  ---')
print('Ingrese su nombre: ')
nombre = str(input())
print('Ingrese su género (H o M)')
genero = str(input())

if genero == 'M':
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es " + grupo)