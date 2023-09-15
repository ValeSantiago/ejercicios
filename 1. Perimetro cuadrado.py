lado = input("Ingresa la medida en centímetros de uno de los lados del cuadrado: ")

try:
    lado = float(lado)
    perimetro = lado * 4
    print(f"El perímetro del cuadrado es: {perimetro} cm.")
except ValueError:
    print("Error: Ingresa un número válido.")



