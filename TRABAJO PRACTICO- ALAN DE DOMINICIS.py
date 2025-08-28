
#Trabajo Practico
#EJERCICIO 1
print ("Hola Mundo")

#EJERCICIO 2

nombre = ("Alan")
print ('Mi nombre es', nombre, '!')

#EJERCICIO 3

nombre=(input('como es tu nombre?'))
apellido= (input(' como es tu apellido?'))
edad=int(input('que edad tienes?'))
residencia= (input(' cual es tu lugar de residencia?')) 
print('soy', nombre , apellido , ', tengo', edad , 'y vivo' , residencia)

#EJERCICIO 4

Radio= float(input('ingrese el Radio'))
area= 3.14 * Radio**2
input(area)

#EJERCICIO 5

segundos=int(input("Ingrese la cantidad de segundos "))
horas= segundos/ 3600
print ('los segundos son', segundos, 'y equivalen a tantas', horas)

#EJERCICIO 6

num=int(input('ingrese el numero que desea saber su tabla'))
print (num,'x1', num*1)
print (num,'x2', num*2)
print (num,'x3', num*3)
print (num,'x4', num*4)
print (num,'x5', num*5)
print (num,'x6', num*6)
print (num,'x7', num*7)
print (num,'x8', num*8)
print (num,'x9', num*9)
print (num,'x10', num*10)

#EJERCICIO 7

num=int(input('ingrese el numero =! de 0'))
num2= int(input('ingrese el numero =! de 0'))
print (num,'+', num2, '=', num+ num2 )
print (num,'-', num2, '=', num- num2 )
print (num,'x', num2, '=', num*  num2 )
print (num,'/', num2, '=', num / num2 )

#EJERCICIO 8

altura=float(input('ingrese cual es su altura en m'))
peso= int (input('ingrese su peso en kg'))
imc= peso/ altura**2
print ('el indice de su masa muscular es', imc)

#EJERCICIO 9

grados= int(input('ingrese los una temperatura en grados celsius'))
fahrenheit= 9/5 * grados + 32
print('Los grados celsius', grados, 'son, y equivalen a tantos', fahrenheit)

#EJERCICIO 10

Num1= float(input("ingrese el primer numero"))
Num2= float(input('ingrese el segundo numero'))
Num3= float (input('ingrese el tercer numero'))
suma= Num1+Num2+Num3
promedio= suma/3
print ('el promedio de los 3 numeros es', promedio)
