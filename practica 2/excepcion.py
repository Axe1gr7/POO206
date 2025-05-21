try:
    numero = int(input("introduce un numero: "))
    resultado = 10 / numero
    print("resultado: ", resultado)
except ValueError:
    print("error se ingreso un valor que no es numero entero.")
except ZeroDivisionError:
    print("error: no se puede dividir entre 0")