print("\nprograma que cuenta las letras de una frase\n")
r=(int)
w=0
while w==0:
    r = int(input("quieres volver a intentar oprime 0 : "))
    if r == 0:
        try:
           frase = input("\ningresa una frase : ")
           if any(char.isdigit() for char in frase):
               raise ValueError("valor no reconocido ingresa solo letras. vuelva a intentar")
           else:
            letra = input("Escribe una letra: ")
            if len(letra) == 1:
                cantidad = frase.count(letra)
                print(f"La letra '{letra}' aparece {cantidad} veces.")
            else:
                print("Debes ingresar solo una letra.")
        except ValueError as error:
            print("error:",error) 
    else:
        print("vuelva pronto")
        break