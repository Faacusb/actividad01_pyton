from impresiones import declarar_comida_favorita

print('Ejercicio 1')
def realizar_calculo():    
    print('Elija la operacion matematica deseada:')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    
    opcion = input('Ingrese el numero de operacion que desea ralizar:')

    if opcion not in ("1", "2", "3", "4"):
        print('Error: Opcion invalida')
        return

    num1 = int(input('Ingrese el primer numero: '))

    num2 = int(input('Ingrese el segundo numero: '))

    if opcion == "1":
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    
    elif opcion == "2":
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")

    elif opcion == "3":
        resultado = num1 * num2
        print(f"El resultado de la multiplicacion es: {resultado}")     

    elif opcion == "4":
        resultado = num1 / num2
        print(f"El resultado de la division es: {resultado}")

realizar_calculo()
print('Fin Ejercicio 1')

print('Ejercicio 2')

def numero_en_orden_ascendente(num):
    num_string = str(num)
    for i in range(len(num_string)-1):
        if num_string[i]> num_string[i + 1]:
            return False
    return True    

print(numero_en_orden_ascendente(6))
print('Fin ejercicio 2')

print('Ejercicio 3')
def numeros_impares_juntos(entrada):
    impares = [str(num) for num in entrada if num % 2 != 0]
    lista_impares = ",".join(impares)
    return lista_impares

entrada = [1,2,3,4,6,7]
print(numeros_impares_juntos(entrada))
print('Fin ejercicio 3')

print('Ejercicio 4')
def lista_elementos_en_comun(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    elementos_en_comun = conjunto1 & conjunto2
    for elemento in elementos_en_comun:
        print(elemento)

celula_animal = ["nucleo", "membrana celular","citoplasma", "mitocondrias", "centriolos"]
celula_vegetal = ["nucleo", "membrana celular", "citoplasma", "mitocondrias", "pared celular", "cloroplastos"]
lista_elementos_en_comun(celula_animal, celula_vegetal)

# print(numero_en_orden(5432))
print('Fin ejercicio 4')

print('Ejercicio 5')
def clave_valida(clave):
   if len(clave)< 6 or len(clave)> 20:
      return False
   
   elif not any(num.isdigit() for num in clave):
      return False
   
   elif " " in clave:
      return False      
   else:
    return True      
   
print(clave_valida("martines1"))
print('Fin ejercicio 5')

print('Ejercicio 6')
def persona_mayor_de_edad(edad):
   return edad >= 18

print(persona_mayor_de_edad(18))
print('Fin Ejercicio 6')

print('Ejercicio 8')
declarar_comida_favorita("Juan", "Milanesa Napolitana")

print('Fin ejercicio 8')

#ejercicio 9
def cuenta_regresiva(entero_positivo):
    if entero_positivo >= 0:
        print(f"{entero_positivo}")
        cuenta_regresiva(entero_positivo - 1)
    
cuenta_regresiva(4)
print('Fin ejercicio 9')

print('Ejercicio 10')
print('(a and b) or True: Resultado True')
print('Fin Ejercicio 10')