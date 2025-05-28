print("\nprograma que hace una cuenta regresiva del numero que ingresa el usuario al 0\n")
r=(int)
w=0
while w==0:
    r = int(input("quieres volver a intentar oprime 0 : "))
    if r == 0:
        try:
           num = int(input("\ningresa un numero : "))
           if num <= 0:
               raise ValueError("valor no reconocido ingresa un numero entero. vuelva a intentar")
           else:
            for i in range(num, -1, -1): 
              if i == 0:
                 print(i)
              else:
                  print(i, end=", ")
        except ValueError as error:
            print("error:",error) 
    else:
        print("vuelva pronto")
        break