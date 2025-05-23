z=0    
while z==0:
    r = int(input("quieres seguir oprime 0: ")) 
    if r== 0: 
        try:
            p= (input("Introduce una palabra:  "))
            p_i = p[::-1]
            if not p.isalpha():
              raise ValueError("Solo se permiten letras.")
            else:
                if p == p_i:
                    print("La palabra es un palindromo")
                else:
                    print("La no palabra es un palindromo")
        except ValueError as letras:
               print("error",letras)
        
    else:
          print("vuelva pronto")
          break