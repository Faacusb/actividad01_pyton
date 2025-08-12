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