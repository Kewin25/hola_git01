def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_cuadrado(lado):
    return lado * lado

def main():
    print("Calculadora de Áreas")
    print("1. Área de un triángulo")
    print("2. Área de un cuadrado")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area}")
    
    elif opcion == "2":
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = calcular_area_cuadrado(lado)
        print(f"El área del cuadrado es: {area}")
    
    elif opcion == "3":
        print("Gracias por usar la calculadora de áreas.")
    
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()