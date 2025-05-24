r=(int)
z=0
    
while z==0:
    r = int(input("quieres seguir oprime 0: ")) 
    if r== 0: 
        try:
            n = int(input("Introduce un año: "))
            error = n != int
            if n % 4 == 0:
                print("El año es bisiesto.")
            else:
             print("El año no es bisiesto.")
        except (ValueError,) as error:
            print(f"Ocurrió un error: ",error)
    else:
          print("vuelva pronto")
          break