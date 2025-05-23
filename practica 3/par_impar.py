r=(int)
z=0
    
while z==0:
    r = int(input("quieres seguir oprime 0: ")) 
    if r== 0: 
        try:
            n = int(input("Introduce un numero: "))
            if n % 2 == 0:
                print("El número es par.")
            else:
             print("El número es impar.")
        except ValueError:print("Debes introducir un número entero válido.")
        
    else:
          print("vuelva pronto")
          break