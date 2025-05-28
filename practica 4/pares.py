print("\nprograma que te da todos los numeros impares del 2 hasta el numero que ingrese el usuario\n")
r=(int)
w=0
while w==0:
    r = int(input("quieres volver a intentar oprime 0 : "))
    if r == 0:
        try:
           num = int(input("\ningresa un numero mayor a 10: "))
           #corroborar si la conraseña tiene 10 caracteres
           if num < 10:
               raise ValueError("Ingresa un numero mayor que 10 . vuelva a intentar")
           else:
             res = " "
             for i in range(2, num):
                 if i % 2 != 0:
                  res += str(i) + ", "
           print("numeros impares que existen desde el 2 hasta",num,":",res)
        except ValueError as error:
            print("error:",error) 
    else:
        print("vuelva pronto")
        break