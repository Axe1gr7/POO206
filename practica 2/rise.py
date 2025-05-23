def v_edad(edad):
    if edad < 18:
        raise ValueError("Eres menor de edad.")
    print("¡Bienvenido! Eres mayor de edad.")

try:
    edad_usuario = int(input("escribe tu edad:   "))
    v_edad(edad_usuario)
except ValueError as error:
    print("Error:", error)