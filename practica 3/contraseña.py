print("\nprograma que genera una contraseña segura\n")
r=(int)
w=0
while w==0:
    r = int(input("quieres volver a intentar oprime 0 : "))
    if r == 0:
        try:
           print("\nTu contrseña debe incluir:\nMas de 10 caracteres \nContener al menos un número \nContener almenos un carácter especial.")
           con = input("\ningresa una contraseña: ")
           #corroborar si la conraseña tiene 10 caracteres
           if len(con) < 10:
               raise ValueError("la contraseña debe tener al menos 10 caracteres. vuelva a intentar")
           else:
           #corroborar que la contraseña tiene un numero 
         
            contiene_num = False
            for num in con:
               if num >= '0' and num <= '9':
                contiene_num = True
                break  
            if not contiene_num:
                raise ValueError ("la contraseña debe tener al menos 1 numero. vuelva a intentar")
       
            #corroborar que al menos tiene un caracter especial
            contiene_sim=False
            sim= "!·$%&/()=?\@#¢∞¬÷"
            for caracter in con:
                if caracter in sim:
                    contiene_sim=True
            if not contiene_sim:
                raise ValueError ("la contraseña debe tener al menos 1 caracter especial. vuelva a intentar")
        #contraseña valida
           print("contraseña valida pase usted.")
        except ValueError as error:
            print("error:",error)      
    else:
        print("vuelva pronto")
        break