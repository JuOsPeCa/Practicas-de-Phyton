#Crear un programa que pida al usuario su nombre, apellido paterno, apellido materno, edad, peso y estatura, desplegarlos en pantalla
#junto con su Índice de Masa Corporal (IMC).

nombre = input('Ingrese su nombre porfavor: ')
apellidoPaterno = input('Ingrese su Primer Apellido porfavor: ')
apellidoMaterno = input('Ingrese su Segundo Apellido porfavor: ')
edad = int(input('Ingrese su Edad porfavor: '))
peso = int(input('Ingrese su Peso actual en Kg porfavor: '))
estatura = float(input('Ingrese su Estatura porfavor: '))
estatura2 = float(estatura * estatura)
IMC = peso/estatura2

print('Nombre del Pasiente: ' + nombre)
print('Primer Apellido del Paseiente: ' + apellidoPaterno)
print('Segundo Apellido del Pasiente: ' + apellidoMaterno)
print('Constando de ' + str(edad) + ' años de edad')
print('Pesando un total de ' + str(peso) + 'Kg')
print('Midiendo un total de ' + str(estatura) + 'mts')
print('Y teniendo un Indice de Masa Corporal (IMC) de ' + str(IMC))