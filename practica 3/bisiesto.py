z=0
    
while z==0:
    r = int(input("quieres seguir oprime 0: ")) 
    if r== 0: 
        try:
            n = int(input("Introduce un año: "))
            if n % 4 == 0:
                print("El número es bisiesto.")
            else:
             print("El número no es bisiesto.")
        except ValueError:print("Debes introducir un año válido.")
        
    else:
          print("vuelva pronto")
          break