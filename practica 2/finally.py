try:
    print("bienvenido a la calculadora de divisiones")
    n1 = int(input("introduce un numero: "))
    n2 = int(input("introduce un numero: "))
    resultado = n1 / n2
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("¡No se puede dividir por cero!")
finally:
    print("Gracias por usar la calculadora de divisiones.")
