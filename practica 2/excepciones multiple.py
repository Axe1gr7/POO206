try:
    numero = int(input("Escribe un número: "))
    resultado = 10 / numero
    print("resultado: ", resultado)
except (ValueError, ZeroDivisionError) as error:
    print(f"Ocurrió un error: {error}")

