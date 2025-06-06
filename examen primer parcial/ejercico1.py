print("programa que solicite un numero par y apartir de ahi su serie ")
r=int
w=int
par=int
vpp=int
w=int(input("quieres seguir presiona el numero 0: "))
while w==0:
       n=int(input("ingresa un par numero del 200 al 400: "))
       try:
            if  n > 200 and n < 400 :            
               print("zzzz")
               r=n/2
               if r > 0:
                   raise (ValueError(print("error el numero no es par"))) 
               else:
                    print("zzzz")     
            else:  
               raise (ValueError(print("error ingresa un numero mayor a 200")))
       except(ValueError):
         break