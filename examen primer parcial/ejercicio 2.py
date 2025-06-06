print("programa que solicite una palabra  ")
r=int
w=int
p=[]
p2=[]
w=int(input("quieres seguir presiona el numero 0: "))
while w==0: 
    try:
             palabra1=(str(input("ingresa una palabra: ")))
             palabra2=(str(input("ingresa otra palabra: ")))
             p=palabra1
             p2=palabra2
             print(p)
             print(p2)
             if p > p2:
                 mas= p>p2  
                 raise(ValueError(print(palabra1,"es mas grande")))
                 
             else:
                 raise(ValueError(print(palabra2,"es mas grande ")))
    except(ValueError):
         break