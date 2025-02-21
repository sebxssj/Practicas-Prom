
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b
def mostrar_menu():
    print("\n--- Calculadora Básica ---") 
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
def ejecutar_calculadora():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige una operación (1-5): "))
            if opcion == 5:
                print("¡Hasta luego!")
                break
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            if opcion == 1:
                resultado = suma(num1, num2)
                print(f"El resultado de la suma es: {resultado}")
            elif opcion == 2:
                resultado = resta(num1, num2)
                print(f"El resultado de la resta es: {resultado}")
            elif opcion == 3:
                resultado = multiplicacion(num1, num2)
                print(f"El resultado de la multiplicación es: {resultado}")
            elif opcion == 4:
                resultado = division(num1, num2)
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
if __name__ == "__main__":
    ejecutar_calculadora()
